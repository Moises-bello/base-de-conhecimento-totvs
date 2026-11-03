---
article_id: 4416663194391
category: Materiais - Compras (SIGACOM)
content_hash: 391a95e3b706c359fa80205a5af1342c05f86852411b6fcbfd562687dca58a19
fetched_at: '2026-06-28T22:41:11.644091+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - FIX – Cadastro
  Fornecedores (Informações Maiúsculas)
type: support-article
updated_at: '2022-10-26T13:49:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416663194391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-FIX-Cadastro-Fornecedores-Informa%C3%A7%C3%B5es-Mai%C3%BAsculas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Ao utilizar a consulta padrão FOR no documento de entrada quando o filtro é por NOME, o sistema não traz o resultado esperado.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Solução**

Ocorre que, ao preencher informações do fornecedor via API Carol, não estão sendo gravados em maiúsculo, fica assim divergente em consultas padrões, e foi foi corrigido na issue DMANMAT02-35608.

* Tratamento para que seja convertida o conta contábil quando informar o código reduzido
* Tratamento para gravar informações do fornecedor em maiúsculo quando utilizado a API Carol.

Boletim: <https://tdn.totvs.com/x/gBWXJg>

Porem, existem inúmeros registros "legados" gravados incorretamente na SA2 dessa forma foi disponibilizado um FIX para converter todos fornecedores digitados em minúsculo pela API CAROL para maiúsculo.

Para correção efetuar os procedimentos:

Aplicar o pacote : FIXSA2\_20211220, anexo.

1. Executar a função U\_FIXSA2(), vai SmartClient;

![u_fix.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416662894615/u_fix.png)

2. Clicar em “Atualizar”, nesse momento será feita a análise dos fornecedores e atualizada a SA2;

![fix-forn.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416670228759/fix-forn.png)

3. Após analisar tabela de fornecedor e verificar que registros foram atualizados e deixando todos em maiúsculo;

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416662927639/Screenshot_2.png)

***Saiba Mais:***

* ***[Grupo de Opcionais](https://tdn.totvs.com/x/UCUMEQ)***
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
