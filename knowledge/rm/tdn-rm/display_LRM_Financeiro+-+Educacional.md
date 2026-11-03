---
content_hash: 4b54fc36ff091d7c639fe1888742b244109a53c39a4df1859bd39ab86f03e285
fetched_at: '2026-06-29T00:09:31.295381+00:00'
page_id: '425458604'
product: rm
source: tdn-rm
title: Financeiro - Educacional
type: documentation
url: https://tdn.totvs.com/display/LRM/Financeiro+-+Educacional
version: 10
---

---

* [Geração de Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=425459455)
* [Valores de Integração Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=425459475)
* [Desconto por Antecipação](https://tdn.totvs.com/pages/viewpage.action?pageId=425459449)
* [Alterar Vencimento do Desconto por Antecipação do Lançamento](https://tdn.totvs.com/pages/viewpage.action?pageId=425459157)
* [Prévia dos Valores do Lançamento](https://tdn.totvs.com/pages/viewpage.action?pageId=425458869)
* [Baixa de Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=425459450)
* [Cancelamento de Baixa de Lançamento com utilização de Valores de Integração](https://tdn.totvs.com/pages/viewpage.action?pageId=425458781)
* [Valor Auxiliar](https://tdn.totvs.com/display/LRM/Valor+Auxiliar)

## 📢 ATENÇÃO: Comunicado Importante – Atualização do TOTVS Educacional

Foram disponibilizados **novos patchs** com uma atualização importante:

12.1.2506.320
12.1.2510.246
12.1.2602.161

### 🔍 O que muda com essa atualização?

Ao abrir o módulo Educacional após a aplicação, será necessária a execução de um processo de **Carga Inicial**. Essa rotina irá alimentar os registros históricos de movimentações financeiras das disciplinas.

ℹ️ **Informação importante sobre a rotina:** Este processo é de **execução única** e **não afetará nenhuma informação ou rotina existente no sistema**. Sua única função é alimentar as novas tabelas de log que foram criadas com os dados atuais já existentes na base.

Esta é a primeira etapa de uma série de novas funcionalidades focadas em garantir a **rastreabilidade total da memória de cálculo** dos lançamentos financeiros gerados.

### ⚖️ O impacto da Reforma Tributária

A manutenção desse histórico e da memória de cálculo tornou-se **crítica e necessária** devido às novas regras previstas na **Reforma Tributária**, que preveem o cálculo do IVA (CBS e IBS) nas operações financeiras. O sistema necessita dessas informações para mapear corretamente a origem dos dados.

#### ⚠️ Pontos de Atenção Críticos:

* **Permissão de Usuário:** O processo de Carga Inicial ficará visível e aparecerá **apenas para usuários que tenham permissão ativa para gerar lançamentos financeiros** no sistema.
* **Ambiente de Homologação:** É altamente recomendável realizar um teste prévio em ambiente de homologação com um backup atualizado da base de produção antes de aplicar o patch no ambiente produtivo.
* **Documentação Completa:** Leia atentamente todos os detalhes técnicos no [Portal TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=1070042189).
