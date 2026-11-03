---
article_id: 360053309294
category: MDT - Atendimento Médico
content_hash: eeba0b0f4a0bcb36e8079567b8618c142dc6ba312018ed5b851da2ff865f1517
fetched_at: '2026-06-28T22:44:20.667863+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como lançar Atestado Médico integrado com Gestão
  de Pessoal
type: support-article
updated_at: '2025-07-25T20:14:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053309294-RH-Linha-Protheus-MDT-Como-lan%C3%A7ar-Atestado-M%C3%A9dico-integrado-com-Gest%C3%A3o-de-Pessoal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24784974306967)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como lançar Atestado Médico integrado com Gestão de Pessoal?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Esta integração irá fornecer à folha de pagamento as informações de controle de ausências na tabela (SR8) (GPEA240), que gerará as horas de afastamento do funcionário.

**1.** Para que a integração possa funcionar corretamente devemos configurar alguns parâmetros, para isto acesse o Configurador (SIGACFG) no seguinte caminho: Ambiente > Cadastro > Parâmetro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089890453)

Localize os parâmetros:   
  
**MV\_NGMDTAF:** Indica se o Sistema irá gerar afastamento para o funcionário, no momento da inclusão de um atestado médico. Se este parâmetro estiver como Não (N) ou se não existir este parâmetro o programa não irá abrir o campo Tipo de Afastamento.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088737034)  
  
**MV\_MDTGPE:** Integração do SIGAMDT com o SIGAGPE, Informar S=Sim ou N=Não    
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088737114)

**MV\_NG2AFAS:** Códigos de afastamentos (movimentação) que podem ser informados pelo médico, no atestado médico.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11735244656535)

Lembrando que a opções informadas no print são apenas exemplo. A empresa pode deixar o parâmetro em branco, ou informar todos os códigos utilizados pela empresa, sempre separando cada código com uma vírgula.

Esses códigos devem ser os mesmos utilizados no campo **Cod.Au.SEFIP** (RCM\_CODSEF) que está localizado na rotina tipos de ausências no SIGAGPE no caminho: atualizações > definições de cálculo > tipos de ausência.  
  
Também é possível visualizar todos os códigos de movimentação no SIGAGPE acessando o caminho: atualizações > definições de cálculo > manutenção de tabela > S046 Códigos de Movimentação.  
  
**2.** Feito a configuração, o lançamento do atestado médico deve estar dentro do período em aberto da folha.  
  
Para gerar o lançamento do atestado médico acesse SIGAMDT ( Módulo 35)  no seguinte caminho: Atualizações > Atendimento Médico > Atestado Médico (MDTA685) > incluir.  
  
Selecione a ficha médica e preencha os campos conforme a necessidade da empresa.  
Aba Atestado:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24802283883543)  
  
Na aba Afastamento, informe o código da Ausência, datas de Saída e Alta, conforme a aba Atestado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24802283888663)  
  
Na Aba Outros, informe o código eSocial.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24802283890967)  
  
Salve o registro e consulte no SIGAGPE o lançamento do atestado e a inclusão do registro na rotina de ausências.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088738154)

A consulta pode ser realizada tanto pelo módulo SIGAMDT , no caminho abaixo:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088738574)  
  
Como pelo Módulo SIGAGPE, no caminho abaixo:  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088738614)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33724298818455)  
  
**Saiba Mais**[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
