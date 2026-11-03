---
article_id: 4575054294295
category: Integrações Outros BackOffice
content_hash: b60613bb5a815218dfc26aa16922e666af2bdc1780b6bc8304e91086481b3d10
fetched_at: '2026-06-28T22:46:42.174084+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - ENTIDOBRIG Obrigatório
  o preenchimento C Custo
type: support-article
updated_at: '2025-02-10T17:34:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4575054294295-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-ENTIDOBRIG-Obrigat%C3%B3rio-o-preenchimento-C-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:44 min****Ocorrência**No módulo da Folha de Pagamento, ao tentar realizar a integração do Lançamento Contábil ao Protheus retorna o erro AJUDA:ENTIDOBRIG Obrigatório o preenchimento da seguinte entidade contábil: C Custo podendo ser Débito ou Crédito.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Essa incidência acontece pois os campos Centro de Custo Débito ou Crédito são obrigatórios no Protheus e devem ser preenchidos no RM para o Protheus receber essa informação.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

O lançamento contábil deve haver o preenchimento do Centro de Custo na coluna Centro de Custo ao editar o Lançamento que está sendo integrado.  
![](https://totvssuporte.zendesk.com/attachments/token/mSuznUax4Tg2h02AQs6ECbw4i/?name=inline269562328.png)​

Para que seja levado automaticamente, devemos preencher na conta contábil essa informação, um modo de identificar qual conta é necessário informar o Centro de Custo que está pendente é verificando o que está sendo contabilizado no RM que pode ser Eventos, Encargos ou ambos.

Para eventos deverá acessar o cadastro do evento em **Administração de Pessoal | Eventos | Eventos** e na aba **Dados Contábeis** exibirá a conta que foi utilizada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4574964947479/mceclip0.png)

Se contabilizar Encargos, acesse **Encargos | Cadastros | Encargos** e edite o encargo para identificar a conta também em **Dados Contábeis**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4574960977943/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4574970102807/mceclip2.png)

Identificando as contas utilizadas para o lançamento, acesse **Encargos | Cadastros Contábeis | Agrupamento de Contas** e edite as contas que identificamos anteriormente, devemos informar o Centro de Custo que será utilizado conforme a imagem abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/docVALCdnmZj45AyBl8kT4zOQ/?name=inline-984897228.png)  
![](https://totvssuporte.zendesk.com/attachments/token/twwQ18E2Qafwn1lIlMGYHr3QE/?name=inline-393505653.png)  
  
Após preencher o Centro de Custo para os agrupamentos, é necessário gerar novamente o Lançamento Contábil, editar o lançamento e verificar se todos os registros foram preenchidos corretamente na coluna Centro de Custo.
