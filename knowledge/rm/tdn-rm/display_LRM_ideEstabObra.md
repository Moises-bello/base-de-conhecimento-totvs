---
content_hash: 0fade0a8a3303f45bf4a02232b005b0fced7716b3a51d6337650aa79eca8ab4e
fetched_at: '2026-06-29T00:11:26.396537+00:00'
page_id: '716358919'
product: rm
source: tdn-rm
title: ideEstabObra
type: documentation
url: https://tdn.totvs.com/display/LRM/ideEstabObra
version: 3
---

## Identificação do Estabelecimento/obra contratante dos Serviços

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| ideEstabObra | infoServTom | 1-1 | - | Identificação do Estabelecimento/obra Tomador dos Serviços | Informações da Filial que efetuou a retenção. |
| tpInscEstab | ideEstabObra | 1-1 | 1 | Preencher com o código correspondente ao tipo de inscrição  Validação: Deve ser igual a [1] (CNPJ) ou [4] CNO | Gerado conforme o campo {nrInscEstab} |
| nrInscEstab | ideEstabObra | 1-1 | 15 | Informar o número de inscrição do estabelecimento conforme o tipo de inscrição indicado no campo {tpInscEstab}.  Validação:  Se {indObra} = [0] preencher com CNPJ contribuinte declarante.  Se {indObra} = [1] informar um número de CNO de propriedade do {cnpjPrestador}.  Se {indObra} = [2] informar um número de CNO de propriedade do contribuinte declarante.   A inscrição informada deve ser compatível com o {tpInscEstab}.  Se {indObra} = [0], o número informado deve ser um CNPJ.  Se {indObra} for igual a [1,2] o número informado deve ser um CNO. | MPRJ.CNOPRJ |
| indObra | ideEstabObra | 1-1 | 1 | Indicativo de Prestação de Serviços em Obra de Construção Civil.  Valores Válidos: 0 - Não é obra de construção civil ou não está sujeita a matrícula de obra; 1 - Obra de Construção Civil - Empreitada Total; 2 - Obra de Construção Civil - Empreitada Parcial;  Validação: Em arquivo gerado por Pessoa Física, deve ser igual a [1,2]. | MCNT.INDPRESTSRV ou MPRJ.INDPRESTSRV   **Origem dos Dados (Hierarquia de Busca):** O preenchimento deste campo segue uma regra de prioridade para garantir a flexibilidade na gestão dos contratos e projetos:   1. **Prioridade 1 (Contrato):** O sistema verifica primeiramente o campo `INDPRESTSRV` na tabela de Contratos (**MCNT**). Se o contrato vinculado ao movimento possuir esta informação preenchida, ela será a origem definitiva para o evento. 2. **Prioridade 2 (Projeto):** Caso o campo no contrato esteja nulo (`NULL`), o sistema buscará o valor configurado no cadastro do Projeto (**MPRJ**), campo `INDPRESTSRV`. |
