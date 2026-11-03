---
content_hash: 1cd26c1c02b9f53e5e3084ec2f0b3865a3b838e413f0f943e1135c0a41784509
fetched_at: '2026-06-29T00:10:11.091601+00:00'
page_id: '452719936'
product: rm
source: tdn-rm
title: Período de Apuração - Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719936
version: 13
---

Neste cadastro são montadas as definições referentes ao período de movimentação que será enviada para o eSocial. O período de apuração é a competência da movimentação que será enviada ao eSocial.

Indicativo de Período de Apuração

* Mensal: Movimentação da Folha Normal.
* Anual: Somente para o 13 Salário.

Ao salvar a inclusão do cadastro, será criada a aba "Eventos da Folha eSocial", onde serão listados os eventos referente a folha de pagamento do trabalhador.

Através dessa aba, poderá ser feita a inclusão, exclusão e manutenção dos eventos: S-1200, S-1210, S-1270,S-1280, S-1298, S-1299 e S-1300, bem como a geração, edição e envio do XML desses eventos para o TAF.

Exclui informação sobre aquisições de produção Rural

Ao selecionar esse campo será gerada a tag <indExcApur1250> no evento S-1299. 

Transmissão Imediata da DCTFWeb 

Ao selecionar este campo será gerada a tag <transDCTFWeb> no evento S-1299.

**Observação:** Tag disponível somente a partir da versão S-1.0.

Valor de Retenção Lei 9711/98

Neste campo deve ser Informado o valor de retenção conforme lei 9711/98 para os casos onde não há integração com Gestão Fiscal.

**Atenção:** Este campo é utilizado na geração do relatório conferência INSS Patronal no campo retenções Total DCTFWeb.

Indicativo de Substituição

Válido apenas para empresa enquadrada nos artigos 7 a 9 da Lei 12.546/2011, conforme classificação tributária indicada no evento de Informações do Empregador.

Percentual de Redução

Será definido como 0 se o Indicativo de Substituição for "Integralmente Substituída", caso contrário o campo estará habilitado para que seja informado o percentual correspondente à razão entre a receita de atividades não relacionadas nos artigos 7 e 8 da Lei 12.546/2011 e a receita bruta total.

Fator Mês e Fator 13º Salário nas Atividades Concomitantes

Somente será habilitado se nas Informações do Empregador a Classificação Tributária for "03 - Empresas enquadradas no regime de tributação Simples com tributação previdenciária substituída e não substituída".

Eventos que utilizam os dados destes cadastro como base para geração das informações: S-1200, S-1210,S-1270, S-1280, S-1298, S-1299 e S-1300.

Atenção

Alguns campos podem estar desabilitados nesses cadastros, pois dependem de regras específicas definidas no leiaute do eSocial:
