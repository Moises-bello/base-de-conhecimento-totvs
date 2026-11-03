---
article_id: 360007819611
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: ef9cd75100c37feb4607058fe5f2b049d32acc78d762aac4de2753738a1d4d0e
fetched_at: '2026-06-28T22:40:32.408207+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Recontabilização das Flags - MV_CTBAPLA
type: support-article
updated_at: '2024-10-14T11:36:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007819611-Cross-Segmento-Backoffice-Linha-Protheus-Recontabiliza%C3%A7%C3%A3o-das-Flags-MV-CTBAPLA
---

**Dúvida**Como limpar as flags  para refazer a contabilização?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**  
Para realizar a limpeza de flags de contabilização, é necessário primeiramente configurar o parâmetro **MV\_CTBAPLA**, e depois [excluir os lançamentos gerados pela contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007062792-MP-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amentos?source=search), conforme segue abaixo sobre remarcação de flags de contabilização em lançamentos contábeis de integração.  
  
1. No ambiente Configurador, opção “Ambiente/Cadastros/Parâmetros”, criar os parâmetros a seguir:

```
Nome: MV_CTBAPLA  
Tipo: Caracter  
Descrição: Indica se o SIGACTB irá apagar os flags de contabilização (_LA / _DTLANC)   
ao excluir lançamentos contábeis.
```

**Observação:** Caso tenha o parâmetro, não é necessário criar o mesmo.   
  
Conteúdos permitidos para configurar a remarcação dos flags de contabilização:  
"1" = Inativo: não limpa os flags nas tabelas de origem do lançamento;  
"2" = Perguntar: pergunta ao usuário se deseja efetuar a remarcação de flags nas tabelas origem de integração;  
"3" = Automático com alertas: remarca/limpa os flags nas tabelas origem de integração sem perguntar ao usuário, exibe alertas caso detecte inconsistências, guarda log dos flags remarcados e não marcados na exclusão;  
"4" = Automático sem alertas, remarca/limpa os flags nas tabelas origem de integração sem perguntar ao usuário, não exibe alertas de inconsistências, guarda log dos flags remarcados e não marcados na exclusão.  
  
**Campos Flags de Contabilização**E1\_LA - Títs. a Receber  
E2\_LA - Títs. a Pagar  
E5\_LA - Mov. Bancário  
EU\_LA - Mov. Caixinha Fin.  
EI\_LA - Aplic./Emprest. Fin.  
EV\_LA - Mult. Natureza  
EZ\_LA - Mult.Natureza x C.Custo  
EF\_LA - Cheques  
F3\_DTLANC - Livros Fiscais  
F2\_DTLANC - NFs  Saída  
F1\_DTLANC - NFs Entrada  
  
**Saiba mais**  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - campo CT2\_FILORI não esta sendo preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018753151-MP-SIGACTB-campo-CT2-FILORI-n%C3%A3o-esta-sendo-preenchido-?source=search)  
[Cross Segmento - Backoffice Linha Protheus - CTBA102 -Exclusão de lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007062792-MP-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amentos?source=search)

[MP - SIGACTB - NÚMERO DE LOTE CONTÁBIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-MP-SIGACTB-N%C3%9AMERO-DE-LOTE-CONT%C3%81BIL?source=search)
