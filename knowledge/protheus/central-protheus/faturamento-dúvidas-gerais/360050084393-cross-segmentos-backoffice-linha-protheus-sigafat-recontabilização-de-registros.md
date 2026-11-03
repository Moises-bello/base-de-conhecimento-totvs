---
article_id: 360050084393
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8ccd701900d95d26fe929b9dc8a390a87b62fe9a537be41e3fef362974662f4c
fetched_at: '2026-06-28T22:38:28.753145+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Recontabilização
  de registros no Faturamento
type: support-article
updated_at: '2023-09-19T12:52:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050084393-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Recontabiliza%C3%A7%C3%A3o-de-registros-no-Faturamento
---

**Dúvida**

Como efetuar a recontabilização de registros no Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Ao usar o parâmetro **MV\_CTBAPLA** com conteúdo diferente de 1 e excluir o registro da contabilização pelas rotinas do Modulo Contábil **CTBA101** (Lançamento Contábil) ou **CTBA102** (Lançamento Contábil Automático), o sistema apagará o conteúdo do campo **F2\_DTLANC** (para notas) e **C5\_DTLANC** (para pedido de vendas) permitindo que a Contabilização seja realizada novamente pelas rotinas específicas.

Para realizar a limpeza de flags de contabilização, é necessário primeiramente configurar o parâmetro **MV\_CTBAPLA**, e depois [excluir os lançamentos gerados pela contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007062792-MP-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amentos?source=search), conforme segue abaixo sobre remarcação de flags de contabilização em lançamentos contábeis de integração.  
  
1. No ambiente Configurador, opção “Ambiente/Cadastros/Parâmetros”, criar os parâmetros a seguir:

```
Nome: MV_CTBAPLA  
Tipo: Caracter  
Descrição: Indica se o SIGACTB irá apagar os flags de contabilização (_LA | _DTLANC)   
ao excluir lançamentos contábeis.
```

**Observação:** Caso tenha o parâmetro, não é necessário criar o mesmo.

Conteúdos permitidos para configurar a remarcação dos flags de contabilização:

* "1" = Inativo: não limpa os flags nas tabelas de origem do lançamento
* "2" = Perguntar: pergunta ao usuário se deseja efetuar a remarcação de flags nas tabelas origem de integração
* "3" = Automático com alertas: remarca/limpa os flags nas tabelas origem de integração sem perguntar ao usuário, exibe alertas caso detecte inconsistências, guarda log dos flags remarcados e não marcados na exclusão
* "4" = Automático sem alertas, remarca/limpa os flags nas tabelas origem de integração sem perguntar ao usuário, não exibe alertas de inconsistências, guarda log dos flags remarcados e não marcados na exclusão

**Campos Flags de Contabilização**

* E1\_LA - Títs. a Receber
* E2\_LA - Títs. a Pagar
* E5\_LA - Mov. Bancário
* EU\_LA - Mov. Caixinha Fin.
* EI\_LA - Aplic./Emprest. Fin.
* EV\_LA - Mult. Natureza
* EZ\_LA - Mult.Natureza x C.Custo
* EF\_LA - Cheques
* F3\_DTLANC - Livros Fiscais
* F2\_DTLANC - NFs  Saída
* F1\_DTLANC - NFs Entrada

**Saiba mais**  
**[Cross Segmento - Backoffice Linha Protheus - SIGACTB - campo CT2\_FILORI não esta sendo preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018753151-MP-SIGACTB-campo-CT2-FILORI-n%C3%A3o-esta-sendo-preenchido-?source=search)**

**[Cross Segmento - Backoffice Linha Protheus - CTBA102 -Exclusão de lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007062792-MP-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amentos?source=search)**

**[MP - SIGACTB - RECONTABILIZAÇÃO DAS FLAGS - MV\_CTBAPLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007819611-MP-SIGACTB-RECONTABILIZA%C3%87%C3%83O-DAS-FLAGS-MV-CTBAPLA?source=search)**

**[MP-FAT-Re contabilização de nota de saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018127532-MP-FAT-Re-contabiliza%C3%A7%C3%A3o-de-nota-de-sa%C3%ADda?source=search)**
