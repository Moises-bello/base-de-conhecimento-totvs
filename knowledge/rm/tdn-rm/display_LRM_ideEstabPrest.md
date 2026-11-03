---
content_hash: 618e83248bb0c83c1480153abb0f8755e0cb0afdee0d6a66dd96522313b2f25b
fetched_at: '2026-06-29T00:11:26.392886+00:00'
page_id: '716358835'
product: rm
source: tdn-rm
title: ideEstabPrest
type: documentation
url: https://tdn.totvs.com/display/LRM/ideEstabPrest
version: 2
---

## Registro que identifica o estabelecimento “prestador” de serviços mediante cessão de mão de obra.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| tpInscEstabPrest | ideEstabPrest | 1-1 | 1 | Preencher com o código correspondente ao tipo de inscrição  Validação: Deve ser igual a [1] (CNPJ) | Valor fixo “1” gerado pelo sistema. |
| nrInscEstabPrest | ideEstabPrest | 1-1 | 15 | Informar o número de inscrição do contribuinte conforme o tipo de inscrição indicado no campo {tpInscEstabPrest}.  Validação: A inscrição informada deve ser compatível com o {tpInscEstabPrest}, e o número informado deve pertencer ao declarante (CNPJ) na base cadastral da RFB | GFILIAL.CGC |
| indObra | ideEstabObra | 1-1 | 1 | Indicativo de Prestação de Serviços em Obra de Construção Civil.  Valores Válidos: 0 - Não é obra de construção civil ou não está sujeita a matrícula de obra; 1 - Obra de Construção Civil - Empreitada Total; 2 - Obra de Construção Civil - Empreitada Parcial;  Validação: Em arquivo gerado por Pessoa Física, deve ser igual a [1,2]. | MCNT.INDPRESTSRV ou MPRJ.INDPRESTSRV   **Origem dos Dados (Hierarquia de Busca):** O preenchimento deste campo segue uma regra de prioridade para garantir a flexibilidade na gestão dos contratos e projetos:   1. **Prioridade 1 (Contrato):** O sistema verifica primeiramente o campo `INDPRESTSRV` na tabela de Contratos (**MCNT**). Se o contrato vinculado ao movimento possuir esta informação preenchida, ela será a origem definitiva para o evento. 2. **Prioridade 2 (Projeto):** Caso o campo no contrato esteja nulo (`NULL`), o sistema buscará o valor configurado no cadastro do Projeto (**MPRJ**), campo `INDPRESTSRV`. |
