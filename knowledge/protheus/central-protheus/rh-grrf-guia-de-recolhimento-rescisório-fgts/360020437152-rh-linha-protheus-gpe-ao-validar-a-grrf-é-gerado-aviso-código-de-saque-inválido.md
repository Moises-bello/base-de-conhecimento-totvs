---
article_id: 360020437152
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 21b56852211b82950b48b837f8587bf04e81a1a5be587f47350beffbef19c220
fetched_at: '2026-06-28T22:43:32.311042+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Ao validar a GRRF é gerado aviso "Código de Saque
  Inválido"
type: support-article
updated_at: '2025-10-20T12:40:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437152-RH-Linha-Protheus-GPE-Ao-validar-a-GRRF-%C3%A9-gerado-aviso-C%C3%B3digo-de-Saque-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069476822039) Tempo aproximado para leitura: **00.03:00 min**

**Ocorrência**Ao validar a GRRF é gerado aviso **Código de Saque Inválido.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão pessoal - A partir da versão 11.80.  
  
**Causa**  
O erro ocorre pois o código de saque na Tabela S043 da rotina Manutenção de Tabelas esta errado em relação ao Código de Afastamento FGTS  
  
**Solução**Quando ocorrer essa situação, verifique na rotina Manutenção Tabelas-**Tabela S043 (versão 12)**, pelo caminho **Atualizações >Def. de Cálculo >Manutenção Tabelas** ou na rotina Parâmetros-**Parâmetro 32 (versão 11**) pelo caminho **Atualizações >Definições de Cálculo >Parâmetros** as informações abaixo:  
1. Coluna **"Cod.Afast. FGTS"**, deve possuir um registro válido, tendo algum código dos listados abaixo:  
Versão 12 Contendo dois Dígitos - Exceto tipo J  
Versão 11 Contendo um dígito

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016723131)     ![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016671452)

2. Na coluna Código A.M. (Saque FGTS) deve ter o código correspondente a coluna **Cod. Afast. FGTS** conforme abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406274933783)

3. Ao calcular a Rescisão, o sistema preencherá na SRA (**Cadastro de Funcionário**) o campo **Cód. Afa. FGTS** que deve possuir a mesma informação do campo **Cod. Afast FGTS** do tipo de Rescisão Utilizado.

**Saiba mais:**

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
