---
content_hash: c20e324e383196d766124f0028f69b6019821f75718df77eb20100748cf4da2a
fetched_at: '2026-06-29T00:06:04.906125+00:00'
page_id: '200912679'
product: rm
source: tdn-rm
title: TTA699_DT_Salario_Composto_Numero_Salario_Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTA699_DT_Salario_Composto_Numero_Salario_Cadastro
version: 1
---

# SALÁRIO COMPOSTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Inclusão de evento em salário composto* |
| **Situação/Requisito:** | *Ao inserir um novo evento de salário composto para o funcionário, o sistema busca o primeiro número de salário disponível para associar ao evento e ao salvar faz a validação se este evento já está associado a outro número de salário ou se o número de salário já está associado a outro evento, apesar do sistema fazer a validação e informar ao usuário que determinado evento não pode ser utilizado, o sistema salva o evento da mesma forma.*  *O cliente também informa que possui muitos professores que utilizam diversos eventos de salário composto e por isso gostaria que ao incluir o evento na tela de salário composto, o sistema já busque no histórico salarial se este evento já consta no histórico salarial e caso sim, já associe ao número de salário correspondente.* |
| **Solução/Implementação:** | *Ao alterar o campo de código do evento, alterar também o campo Número do Salário para utilizar o número já vinculado a este evento pelo histórico salarial.* |
| **Chamados relacionados:** | *TTA699* |
| **Versões/Release:** | *11.82.41* |
