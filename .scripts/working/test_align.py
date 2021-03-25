import align

fruits1 = [
    ('apple', 1),
    ('orange', 2),
    ('banana', 3),
    ('pineapple', 4)
]

fruits2 = [
    ('apple', 1),
    ('orange', 2),
    ('bananas', 3),
    ('pineapple', 4)
]

fruits3 = [
    ('apple', 1),
    ('orange', 2),
    ('banana', 3),
    ('mango', 4),
    ('pineapple', 5),
]

fruits4 = [
    ('apple', 1),
    ('banana', 2),
    ('mango', 3),
    ('pineapple', 4),
]

sample_current_data = [('aṃguttaranikāya', 'an1.1:0.1'),
    ('rūpādivagga', 'an1.1:0.2'),
    ('', 'an1.10:1.0'),
    ('evaṃmesutaṃ', 'an1.1:1.1'),
    ('ekaṃsamayaṃbhagavāsāvatthiyaṃviharatijetavaneanāthapiṇḍikassaārāme',
    'an1.1:1.2'),
    ('tatrakhobhagavābhikkhūāmantesi', 'an1.1:1.3'),
    ('bhikkhavoti', 'an1.1:1.4'),
    ('bhadantetitebhikkhūbhagavatopaccassosuṃ', 'an1.1:1.5'),
    ('bhagavāetadavoca', 'an1.1:1.6'),
    ('nāhaṃbhikkhaveaññaṃekarūpampisamanupassāmiyaṃevaṃpurisassacittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhaveitthirūpaṃ',
    'an1.1:2.1'),
    ('itthirūpaṃbhikkhavepurisassacittaṃpariyādāyatiṭṭhatīti', 'an1.1:2.2'),
    ('paṭhamaṃ', 'an1.1:2.3'),
    ('nāhaṃbhikkhaveaññaṃekasaddampisamanupassāmiyaṃevaṃpurisassacittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhaveitthisaddo',
    'an1.2:1.1'),
    ('itthisaddobhikkhavepurisassacittaṃpariyādāyatiṭṭhatīti', 'an1.2:1.2'),
    ('dutiyaṃ', 'an1.2:1.3'),
    ('nāhaṃbhikkhaveaññaṃekagandhampisamanupassāmiyaṃevaṃpurisassacittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhaveitthigandho',
    'an1.3:1.1'),
    ('itthigandhobhikkhavepurisassacittaṃpariyādāyatiṭṭhatīti', 'an1.3:1.2'),
    ('tatiyaṃ', 'an1.3:1.3'),
    ('nāhaṃbhikkhaveaññaṃekarasampisamanupassāmiyaṃevaṃpurisassacittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhaveitthiraso',
    'an1.4:1.1'),
    ('itthirasobhikkhavepurisassacittaṃpariyādāyatiṭṭhatīti', 'an1.4:1.2'),
    ('catutthaṃ', 'an1.4:1.3'),
    ('nāhaṃbhikkhaveaññaṃekaphoṭṭhabbampisamanupassāmiyaṃevaṃpurisassacittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhaveitthiphoṭṭhabbo',
    'an1.5:1.1'),
    ('itthiphoṭṭhabbobhikkhavepurisassacittaṃpariyādāyatiṭṭhatīti', 'an1.5:1.2'),
    ('pañcamaṃ', 'an1.5:1.3'),
    ('nāhaṃbhikkhaveaññaṃekarūpampisamanupassāmiyaṃevaṃitthiyācittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhavepurisarūpaṃ',
    'an1.6:1.1'),
    ('purisarūpaṃbhikkhaveitthiyācittaṃpariyādāyatiṭṭhatīti', 'an1.6:1.2'),
    ('chaṭṭhaṃ', 'an1.6:1.3'),
    ('nāhaṃbhikkhaveaññaṃekasaddampisamanupassāmiyaṃevaṃitthiyācittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhavepurisasaddo',
    'an1.7:1.1'),
    ('purisasaddobhikkhaveitthiyācittaṃpariyādāyatiṭṭhatīti', 'an1.7:1.2'),
    ('sattamaṃ', 'an1.7:1.3'),
    ('nāhaṃbhikkhaveaññaṃekagandhampisamanupassāmiyaṃevaṃitthiyācittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhavepurisagandho',
    'an1.8:1.1'),
    ('purisagandhobhikkhaveitthiyācittaṃpariyādāyatiṭṭhatīti', 'an1.8:1.2'),
    ('aṭṭhamaṃ', 'an1.8:1.3'),
    ('nāhaṃbhikkhaveaññaṃekarasampisamanupassāmiyaṃevaṃitthiyācittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhavepurisaraso',
    'an1.9:1.1'),
    ('purisarasobhikkhaveitthiyācittaṃpariyādāyatiṭṭhatīti', 'an1.9:1.2'),
    ('navamaṃ', 'an1.9:1.3'),
    ('nāhaṃbhikkhaveaññaṃekaphoṭṭhabbampisamanupassāmiyaṃevaṃitthiyācittaṃpariyādāyatiṭṭhatiyathayidaṃbhikkhavepurisaphoṭṭhabbo',
    'an1.10:1.1'),
    ('purisaphoṭṭhabbobhikkhaveitthiyācittaṃpariyādāyatiṭṭhatīti', 'an1.10:1.2'),
    ('dasamaṃ', 'an1.10:1.3'),
    ('rūpādivaggopaṭhamo', 'an1.10:1.4')]

stale_data = [('Aṅguttara Nikāya 1', 'an1.1-10:0.1', 'Aṅguttara Nikāya 1'),
    ('1. Rūpādivagga', 'an1.1-10:0.2', '1. Imagens, etc.'),
    ('1', 'an1.1-10:0.3', '1'),
    ('Evaṃ me sutaṃ—\u200b', 'an1.1-10:1.1.1', 'Assim ouvi.'),
    ('ekaṃ samayaṃ bhagavā sāvatthiyaṃ viharati jetavane anāthapiṇḍikassa ārāme.',
    'an1.1-10:1.1.2',
    'Em certa ocasião o Buda estava perto de Savatthi, no Bosque de Jeta, no Parque de Anathapindika.'),
    ('Tatra kho bhagavā bhikkhū āmantesi:',
    'an1.1-10:1.1.3',
    'Lá o Buda se dirigiu aos bhikkhus:'),
    ('“bhikkhavo”ti.', 'an1.1-10:1.1.4', '"Bhikkhus!"'),
    ('“Bhadante”ti te bhikkhū bhagavato paccassosuṃ.',
    'an1.1-10:1.1.5',
    '"Venerável Senhor", eles responderam.'),
    ('Bhagavā etadavoca:', 'an1.1-10:1.1.6', 'O Buda disse o seguinte:'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekarūpampi samanupassāmi yaṃ evaṃ purisassa cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, itthirūpaṃ.',
    'an1.1-10:1.2.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de um homem do que a imagem de uma mulher.'),
    ('Itthirūpaṃ, bhikkhave, purisassa cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:1.2.2',
    'De fato, tal imagem ocupa a mente de um homem."'),
    ('Paṭhamaṃ.', 'an1.1-10:1.2.3', ' '),
    ('2', 'an1.1-10:1.2.4', '2'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekasaddampi samanupassāmi yaṃ evaṃ purisassa cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, itthisaddo.',
    'an1.1-10:2.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de um homem do que o som de uma mulher.'),
    ('Itthisaddo, bhikkhave, purisassa cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:2.1.2',
    'De fato, tal som ocupa a mente de um homem."'),
    ('Dutiyaṃ.', 'an1.1-10:2.1.3', ' '),
    ('3', 'an1.1-10:2.1.4', '3'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekagandhampi samanupassāmi yaṃ evaṃ purisassa cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, itthigandho.',
    'an1.1-10:3.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de um homem do que o aroma de uma mulher.'),
    ('Itthigandho, bhikkhave, purisassa cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:3.1.2',
    'De fato, tal aroma ocupa a mente de um homem."'),
    ('Tatiyaṃ.', 'an1.1-10:3.1.3', ' '),
    ('4', 'an1.1-10:3.1.4', '4'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekarasampi samanupassāmi yaṃ evaṃ purisassa cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, itthiraso.',
    'an1.1-10:4.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de um homem do que o sabor de uma mulher.'),
    ('Itthiraso, bhikkhave, purisassa cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:4.1.2',
    'De fato, tal sabor ocupa a mente de um homem."'),
    ('Catutthaṃ.', 'an1.1-10:4.1.3', ' '),
    ('5', 'an1.1-10:4.1.4', '5'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekaphoṭṭhabbampi samanupassāmi yaṃ evaṃ purisassa cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, itthiphoṭṭhabbo.',
    'an1.1-10:5.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de um homem do que o toque de uma mulher.'),
    ('Itthiphoṭṭhabbo, bhikkhave, purisassa cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:5.1.2',
    'De fato, tal toque ocupa a mente de um homem."'),
    ('Pañcamaṃ.', 'an1.1-10:5.1.3', ' '),
    ('6', 'an1.1-10:5.1.4', '6'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekarūpampi samanupassāmi yaṃ evaṃ itthiyā cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, purisarūpaṃ.',
    'an1.1-10:6.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de uma mulher do que a imagem de um homem.'),
    ('Purisarūpaṃ, bhikkhave, itthiyā cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:6.1.2',
    'De fato, tal imagem ocupa a mente de uma mulher."'),
    ('Chaṭṭhaṃ.', 'an1.1-10:6.1.3', ' '),
    ('7', 'an1.1-10:6.1.4', '7'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekasaddampi samanupassāmi yaṃ evaṃ itthiyā cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, purisasaddo.',
    'an1.1-10:7.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de uma mulher do que o som de um homem.'),
    ('Purisasaddo, bhikkhave, itthiyā cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:7.1.2',
    'De fato, tal som ocupa a mente de uma mulher."'),
    ('Sattamaṃ.', 'an1.1-10:7.1.3', ' '),
    ('8', 'an1.1-10:7.1.4', '8'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekagandhampi samanupassāmi yaṃ evaṃ itthiyā cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, purisagandho.',
    'an1.1-10:8.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de uma mulher do que o aroma de um homem.'),
    ('Purisagandho, bhikkhave, itthiyā cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:8.1.2',
    'De fato, tal aroma ocupa a mente de uma mulher."'),
    ('Aṭṭhamaṃ.', 'an1.1-10:8.1.3', ' '),
    ('9', 'an1.1-10:8.1.4', '9'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekarasampi samanupassāmi yaṃ evaṃ itthiyā cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, purisaraso.',
    'an1.1-10:9.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de uma mulher do que o sabor de um homem.'),
    ('Purisaraso, bhikkhave, itthiyā cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:9.1.2',
    'De fato, tal sabor ocupa a mente de uma mulher."'),
    ('Navamaṃ.', 'an1.1-10:9.1.3', ' '),
    ('10', 'an1.1-10:9.1.4', '10'),
    ('“Nāhaṃ, bhikkhave, aññaṃ ekaphoṭṭhabbampi samanupassāmi yaṃ evaṃ itthiyā cittaṃ pariyādāya tiṭṭhati yathayidaṃ, bhikkhave, purisaphoṭṭhabbo.',
    'an1.1-10:10.1.1',
    '"Bhikkhus, não há algo que ocupe mais a mente de uma mulher do que o toque de um homem.'),
    ('Purisaphoṭṭhabbo, bhikkhave, itthiyā cittaṃ pariyādāya tiṭṭhatī”ti.',
    'an1.1-10:10.1.2',
    'De fato, tal toque ocupa a mente de uma mulher."'),
    ('Dasamaṃ.', 'an1.1-10:10.1.3', ' '),
    ('Rūpādivaggo paṭhamo.', 'an1.1-10:10.1.4', ' ')]

result = align.align(sample_current_data, stale_data)

def align_pt(current, stale):
    mapping = align.root_alignment_mapping(current, stale)
    result = {}
    lost_strings = {}
    reverse_mapping = {v:k for k,v in mapping.items()}
    for root_string, uid, pt_string in stale:
        new_uid = mapping.get(uid)
        if not new_uid:
            lost_strings[uid] = {'pli': root_string, 'pt': pt_string}
            continue
        result[new_uid] = pt_string
    

    return (result, lost_strings)