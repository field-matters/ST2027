from glossing import evaluate_glosses


def evaluate_gloss_list(pred_gloss, gold_gloss):
    '''Evaluate a list of glossed sentences (list of strings).'''

    eval_gloss = evaluate_glosses(
        predicted_glosses=pred_gloss,
        gold_glosses=gold_gloss,
        )

    score_dict = {
        'MER': eval_gloss['morphemes']['error_rate'],
        'Morpheme accuracy': eval_gloss['morphemes']['accuracy'],
        'Word accuracy': eval_gloss['words']['accuracy']
    }

    return score_dict