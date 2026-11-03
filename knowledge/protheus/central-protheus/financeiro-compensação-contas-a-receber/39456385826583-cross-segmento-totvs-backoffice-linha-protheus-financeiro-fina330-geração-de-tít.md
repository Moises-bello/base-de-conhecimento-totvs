---
article_id: 39456385826583
category: Financeiro - Compensação Contas a Receber
content_hash: 29c0d6dea5e7b0e5517d0dadcf244db09772299f17dc33eedb8c1ab5423f988a
fetched_at: '2026-06-28T22:37:40.461447+00:00'
product: protheus
section_id: 35056224784407
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 -
  Geração de título de IR em duplicidade na compensação do Contas a Receber
type: support-article
updated_at: '2026-04-07T11:50:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39456385826583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-FINA330-Gera%C3%A7%C3%A3o-de-t%C3%ADtulo-de-IR-em-duplicidade-na-compensa%C3%A7%C3%A3o-do-Contas-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39456385815447) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Por que o sistema gera um novo título de IR (Imposto de Renda) durante o processo de compensação de contas a receber (FINA330), mesmo quando o imposto já foi retido e gerado no momento da emissão do título original?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Este comportamento ocorre devido a uma alteração cadastral no registro do Cliente após a emissão do título principal, mas antes da realização da compensação.

Se no momento da inclusão do título de receita o cliente estava configurado para reter o IR na **Emissão**, o sistema gera o título de imposto imediatamente. Caso o cadastro do cliente seja alterado posteriormente para que a retenção ocorra na **Baixa** (ou vice-versa), o motor de cálculo de impostos identificará a divergência durante a rotina de Compensação (CP). Como a compensação é interpretada pelo sistema como um movimento de baixa, ele processará a regra vigente no cadastro do cliente no momento da execução, resultando em uma nova retenção indevida ou duplicada.

Para garantir a integridade dos dados, a configuração de retenção de impostos no cadastro de clientes não deve ser alterada enquanto houver títulos em aberto que utilizem regras distintas.

**Passos**

1. Acesse o módulo **Financeiro** (SIGAFIN);
2. Vá em **Atualizações** > **Cadastros** > **Clientes** (MATA030);
3. Localize o cliente envolvido e clique em **Alterar**;
4. Verifique na aba **Fiscais** (ou conforme o dicionário de dados local) os campos de configuração de retenção de impostos (Ex: IRRF na Baixa);
5. Certifique-se de que a configuração está condizente com a regra de negócio aplicada no momento da emissão dos títulos que serão compensados;
6. Caso a alteração tenha sido feita por erro, reverta o parâmetro para o estado original antes de processar a compensação no **Contas a Receber** (FINA330).
