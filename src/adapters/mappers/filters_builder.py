from typing import List
from adapters.mappers.controller_change_mapper import CONTROLLER_CHANGE_MAPPER
from adapters.mappers.note_translator import translate_note_to_midi_code
from midifilter.filters import ControllerChange, MidiFilter, NoteRange, Transpose, VelocityRange
from model.configuration.layer_config import LayerConfig
from model.configuration.performance_config import PerformanceConfig


class FiltersBuilder:

    def build_filters_from_performance(self, performance_config: PerformanceConfig) -> List[MidiFilter]:

        filters = []
        for layer in performance_config.layers:
            if layer.active:

                note_range_filter = self.__build_note_range_filter(layer)
                transpose_filter = self.__build_transpose_filter(layer)
                velocity_range_filter = self.__build_velocity_range_filter(layer)

                note_range_filter.set_successor_filter(transpose_filter)
                transpose_filter.set_successor_filter(velocity_range_filter)

                filters.append(note_range_filter)

                filters = filters + self.__build_controller_change_filter_list(layer)

        return filters

    def __build_velocity_range_filter(self, layer: LayerConfig) -> VelocityRange:
        return VelocityRange(
            lower=layer.velocity_range_config.min_velocity,
            upper=layer.velocity_range_config.max_velocity,
            channel=layer.channel)

    def __build_note_range_filter(self, layer: LayerConfig) -> NoteRange:
        return NoteRange(            
            lower=translate_note_to_midi_code(layer.note_range_config.lower_key),
            upper=translate_note_to_midi_code(layer.note_range_config.upper_key),
            channel=layer.channel)

    def __build_transpose_filter(self, layer: LayerConfig) -> Transpose:
        transpose = layer.transportation + layer.octave * 12
        return Transpose(
            transpose=transpose,
            channel=layer.channel)

    def __build_controller_change_filter_list(self, layer: LayerConfig) -> List[ControllerChange]:
        controller_change_filters = []
        for cc in layer.controller_changes:            
            controller_change_filters.append(
                ControllerChange(
                    cc=CONTROLLER_CHANGE_MAPPER[cc.continues_controller],
                    min_=cc.min, 
                    max_=cc.max,
                    channel=layer.channel)
                )
        return controller_change_filters
