def fake_performance_configuration():
    return {
        "number": 1,
        "name": "Performance Name",
        "tempo_config": {
            "min_bpm": 40,
            "max_bpm": 250
        },
        "time_signature": {
            "beats_per_bar": 3,
            "beat_unit": 4
        },
        "layers": [
            {
                "number": 1,
                "active": True,
                "channel": 1,
                "program": 2,
                "octave": -1,
                "transpose": 12,
                "fix_velocity": 100,
                "keep_note_on_until_touch_it_again": False,
                "note_range_config": {
                    "lower_key": "C-1",
                    "upper_key": "B5"
                },
                "velocity_range_config": {
                    "max_velocity": 127,
                    "min_velocity": 0
                },
                "controller_changes": [
                    {
                        "continues_controller": "BANK_SELECT",
                        "min": 80,
                        "max": 81
                    },
                    {
                        "continues_controller": "BANK_SELECT_LSB",
                        "min": 0,
                        "max": 3
                    },
                    {
                        "continues_controller": "SUSTAIN",
                        "min": 0,
                        "max": 127,
                        "use_global_channel": True
                    },
                    {
                        "continues_controller": "VOLUME",
                        "min": 0,
                        "max": 127
                    },
                    {
                        "continues_controller": "EXPRESSION",
                        "min": 0,
                        "max": 127
                    }
                ]
            },
            {
                "number": 2,
                "active": True,
                "channel": 2,
                "note_range_config": {
                    "lower_key": "C6",
                    "upper_key": "C8"
                },
                "velocity_range_config": {
                    "max_velocity": 127,
                    "min_velocity": 0
                },
                "keep_note_on_until_touch_it_again": True,
                "controller_changes": [
                    {
                        "continues_controller": "BANK_SELECT",
                        "min": 80,
                        "max": 81
                    },
                    {
                        "continues_controller": "BANK_SELECT_LSB",
                        "min": 0,
                        "max": 3
                    },
                    {
                        "continues_controller": "SUSTAIN",
                        "min": 0,
                        "max": 127,
                        "use_global_channel": True
                    },
                    {
                        "continues_controller": "VOLUME",
                        "min": 0,
                        "max": 127
                    },
                    {
                        "continues_controller": "EXPRESSION",
                        "min": 0,
                        "max": 127
                    }
                ]
            },
            {
                "number": 3,
                "active": True,
                "channel": 3,
                "note_range_config": {
                    "lower_key": "C-1",
                    "upper_key": "B5"
                },
                "velocity_range_config": {
                    "max_velocity": 127,
                    "min_velocity": 80
                },
                "controller_changes": [
                    {
                        "continues_controller": "BANK_SELECT",
                        "min": 80,
                        "max": 81
                    },
                    {
                        "continues_controller": "BANK_SELECT_LSB",
                        "min": 0,
                        "max": 3
                    },
                    {
                        "continues_controller": "SUSTAIN",
                        "min": 0,
                        "max": 127,
                        "use_global_channel": True
                    },
                    {
                        "continues_controller": "VOLUME",
                        "min": 0,
                        "max": 127
                    },
                    {
                        "continues_controller": "EXPRESSION",
                        "min": 0,
                        "max": 127
                    }
                ]
            }
        ]
    }
