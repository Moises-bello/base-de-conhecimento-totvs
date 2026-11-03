---
article_id: 25083216879511
category: Evento S-2221
content_hash: 272b5b05cfd43136d4e2e7f9ba69e83e50f9efdf5226c66a42c29f3c0a1c2a4b
fetched_at: '2026-06-28T22:45:22.607806+00:00'
product: protheus
section_id: 25082252387351
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2221 - Como gerar o evento S-2221 Exame
  Toxicológico
type: support-article
updated_at: '2026-05-13T19:03:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25083216879511-RH-Linha-Protheus-MDT-eSocial-S-2221-Como-gerar-o-evento-S-2221-Exame-Toxicol%C3%B3gico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25083216862615) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como gerar o evento S-2221 Exame Toxicológico?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**  
O envio do evento é gerado através dos dados da rotina Exames do Funcionário (MDTA120) do módulo SIGAMDT.  
  
**Quem está obrigado:**  
O empregador que tenha contratado motorista profissional empregado de transporte rodoviário coletivo de passageiros e de transporte rodoviário de cargas.  
  
**Pré requisitos:**  
Envio dos eventos S-2190 ou S-2200 do respectivo vínculo trabalhista.  
  
**Observação**:  
Apenas os exames realizados após o início da obrigatoriedade de envio deste evento **01/08/2024 serão registrados no eSocial**.  
  
**Como gerar?**  
  
**1.** Incluir o Exame Toxicológico na rotina de Exames (Atualizações > PCMSO > Exames (MDTA020).   
  
**Obs.:** O campo "Proc. Realiz." (TM4\_PROCRE) não será incluído no evento S-2221 por enquanto, mas ele faz parte do evento S-2220, que é obrigatório e se faz necessário o preenchimento.

Quando for necessário criar um novo exame para envio do evento S-2221, a empresa precisará incluir um código que referencia a Tabela 27 do eSocial. O suporte não pode orientar sobre qual opção deve ser utilizada, então é importante que você consulte o Sesmt da empresa para obter as orientações necessárias.

Consulte nossa documentação: [Qual código deve ser utilizado no exame para envio do evento S-2221 Exame Toxicológico para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25415291343383-RH-Linha-Protheus-MDT-eSocial-S-2221-Qual-c%C3%B3digo-deve-ser-utilizado-no-exame-para-envio-do-evento-S-2221-Exame-Toxicol%C3%B3gico-para-o-eSocial)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25666697858455)  
  
**2.** Vincular o exame ao Fornecedor de Exames (MDTA045). Atualizações > PCMSO > Fornecedor Exames.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26358775052695)  
  
**3.** Incluir Médico Emitente de Atestado. Atualizações > Atendimento Médico > Médicos Emit. Atestado (MDTA680).  
  
Deve ser informado todos os campos, com atenção no **nome Emitente, Num. Ent. e UF Ent**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26358748707351)

**4.** Incluir Exames do Funcionário. Atualizações > PCMSO > Exames do Funcionário (MDTA120). Deverá preencher todos os campos destacado na imagem.   
  
Observações:   
  
O campo **"Origem Exame"** deve ser do tipo **ASSISTENCIAL**.  
O campo **"Seq. Exame"** deve ser preenchido no **formato padrão do eSocial AA999999999**.  
O campo **"Med. Exam."** deve ser preenchido e é habilitado após incluir informação no campo **"Cod DENATRAN".**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40449193835031)  
  
Após preencher as informações e clicar em CONFIRMAR, não havendo inconsistências, será apresentado a mensagem de integração:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25083216867095)  
  
Para confirmar as informações integradas, acesse o módulo TAF (84) e acesse a rotina Atualizações > Não Periódicos > Exame Toxicológico do Mot. Profissional (TAFA528).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26358775085335)  
  
Deve conferir as informações antes de enviar ao Governo:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26358748721047)  
  
Certifique que o Ambiente esta atualizado conforme orientação do artigo: [Como se adequar e atualizar o ambiente para nota técnica S-1.2 Nº 03/2024 referente o evento S-2221](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25082795447191)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
