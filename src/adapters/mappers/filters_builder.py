from typing import List
from adapters.mappers.note_translator import translate_note_to_midi_code
from midifilter.filters import MidiFilter, NoteRange, Transpose, VelocityRange
from model.configuration.layer_config import LayerConfig
from model.configuration.performance_config import PerformanceConfig


class FiltersBuilder:

    def build_filters_from_performance(self, performance_config: PerformanceConfig) -> List[MidiFilter]:

        filters = []
        for layer in performance_config.layers:
            if layer.active:
                filters.append(self.__build_velocity_range_filter(layer))
                filters.append(self.__build_note_range_filter(layer))
                transpose_filter = self.__build_transpose_filter(layer)
                if not transpose_filter is None:
                    filters.append(transpose_filter)
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
        if transpose != 0:
           return Transpose(
               transpose=transpose,
               channel=layer.channel)
        return None
