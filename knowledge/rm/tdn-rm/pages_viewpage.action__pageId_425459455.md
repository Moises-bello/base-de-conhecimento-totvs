---
content_hash: 1b8dddbfe3912e26571ba21f96ecc119d4026f37435fb52f612afc6b5e220c47
fetched_at: '2026-06-29T00:09:36.001025+00:00'
page_id: '425459455'
product: rm
source: tdn-rm
title: Geração de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459455
version: 85
---

---

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
