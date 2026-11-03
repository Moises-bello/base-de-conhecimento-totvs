---
article_id: 360016130991
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 724a111308da01a47434dddb02073feabdf9743ae8ab60f6282cd24059fb20d5
fetched_at: '2026-06-28T22:38:28.610048+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - NFe 4.0 - Novo
  Layout SEFAZ - Principais dúvidas em relação à operação no módulo Faturamento
type: support-article
updated_at: '2023-07-05T18:25:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016130991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-NFe-4-0-Novo-Layout-SEFAZ-Principais-d%C3%BAvidas-em-rela%C3%A7%C3%A3o-%C3%A0-opera%C3%A7%C3%A3o-no-m%C3%B3dulo-Faturamento
---

**Dúvida**

NFe 4.0 - Novo Layout SEFAZ - O que muda? Principais dúvidas em relação à operação no módulo Faturamento.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Segue algumas das dúvidas mais recorrentes em relação ao módulo faturamento:

**1 - Os Tipos de Frete disponíveis no Protheus atendem às opções da NT?**  
R: Sim. A implementação requer aplicação do dicionário de dados: <https://suporte.totvs.com/portal/p/10098/download?e=688783>

**2 - O que foi alterado em relação à transportadora e Placa do veículo?**  
R: Houve alteração de conceito pela Sefaz. Para o layout 4.00 a Sefaz criou a seguinte rejeição 868: Grupo veículo transporte e reboque não devem ser informados.

Para a nova rejeição ocorrerá o seguinte tratamento no fonte da NFESEFAZ: Para operações interestaduais não será mais levado conteúdo para a TAG para nenhuma UF (alteração direto no NFESEFAZ).

**3- Na NFe 4.0 será necessário informar: A Forma de pgto (A vista / A prazo) – TAG <indPag> e o Meio de pgto (Cartão/boleto/etc.) – TAG <tpag>**

**3A - Hoje o que o SEFAZ determina por “Meio de pgto” é para o Protheus a "Forma de Pgto"; ou seja cartão, boleto, etc.**

R: Está sendo estudado, mas no momento não será alterada a nomenclatura. Este dado continua sendo buscado do cadastro "Forma de Pgto" conforme detalhes no item 4 a seguir. Ressaltando que a nomenclatura (descrição “Forma de Pgto”) do campo não interfere neste processo e que o sistema não atende apenas a nota mercantil.

**3B - O XML busca a FORMA (A vista / prazo) de onde?**

R: É realizado um tratamento direto no fonte NFESEFAZ. É verificada a data da emissão da Nota e considerado "A vista" se os campos E1\_VENCORI e F2\_EMISSAO estão com a mesma data e se possui apenas uma parcela. Do contrário se considera "A prazo".

**4 - Onde o “Meio” deve ser informado para levar à NFe (Cartão/boleto/etc.) – TAG <tpag> ?**  
R: Deve ser informado no campo E4\_FORMA agora disponível no módulo Faturamento (Cadastro de Cond. Pgto) conforme ISSUE DSERFAT-6169.

Documentação: [FAT0105\_Formas de Pagamento no Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=243648380)

Para saber sobre outras dúvidas em relação a NFE 4.0, acesse: **[NFe 4.0 - Novo Layout SEFAZ - O que muda? Principais dúvidas em relação à operação no módulo Faturamento.](http://tdn.totvs.com/pages/viewpage.action?pageId=379309314)**
