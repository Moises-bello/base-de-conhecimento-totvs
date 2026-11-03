---
article_id: 27704324254743
category: eSocial
content_hash: ee82a03ea83195f2976942b991fbb6cda3f3d22ebd7027327a576c3319bde9b4
fetched_at: '2026-06-28T22:47:39.033883+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2240 - Erro: O campo ''docAval'' do registro ''epi'' é obrigatório
  e não está preenchido.'
type: support-article
updated_at: '2025-09-25T14:50:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27704324254743-RH-RM-SMT-S-2240-Erro-O-campo-docAval-do-registro-epi-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27704308980759) Tempo aproximado para leitura: **00****:02:30 min****Ocorrência**Ao gerar o XML do evento S-2240 aparece a seguinte mensagem: *O campo 'docAval' do registro 'epi' é obrigatório e não está preenchido*. O que fazer?  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - 12.1.28 e superiores  
  
**Causa**A mensagem de erro é emitida quando no cadastro dos Lotes dos EPI's que foram vinculados ao funcionário não possuem o campo **'CA/Documento de Avaliação'** preenchido e/ou as datas não estão válidas para o período de envio do evento S-2240.    
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27704308982039)  
  
**Solução**Para correção do erro, será necessário validar como está parametrizado as Condições Ambientais de Trabalho. Dessa forma, deve acessar o módulo **SSO** | **Opções** | **Parametrizador** | **Etapa eSocial - SST** | **Condições Ambientais de Trabalho** e verificar se o parâmetro estará marcado ou desmarcado.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27704927648023)

**1** - Quando o parâmetro '**Consiste EPI através do Risco, Nível de Risco e Avaliação de Risco**' está marcado, é necessário validar se o campo CA localizado no cadastro do Lote está preenchido e se as datas estão corretas, e está validação deve ser feita no cadastro do Risco, Nível de Risco e/ou Avaliação de Risco vinculada ao funcionário. Isso irá depender de qual destes cadastros incluíram EPI's.   
  
**- EPI's vinculados ao Risco:**

Acesse **PPRA/PGR** | **Riscos** | **Anexos** | **EPI/EPC  
  
![](https://totvssuporte.zendesk.com/attachments/token/4ptg1fYwYQDd3VGK7lPWMCR5E/?name=image.png)**

**![](https://totvssuporte.zendesk.com/attachments/token/zKYUOgNnm9ReNniq9xiYWlqlp/?name=image.png)**

**![](https://totvssuporte.zendesk.com/attachments/token/fYyvWo4lmbyszRlZxH6pDtnKS/?name=image.png)**

**- EPI's vinculados ao Nível do Risco:**

Acesse o cadastro do **Risco** | **Anexos** | **Nível de Risco** | **Edite o Nível do Risco** | **Anexos** | **EPI Nível de Risco**

**![](https://totvssuporte.zendesk.com/attachments/token/UVaUKlIA2ES00cVQQVNhq9Mh4/?name=image.png)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27704324250135)**

**![](https://totvssuporte.zendesk.com/attachments/token/Tu3Sxl8M6VpXJkhh6vdYfyuS2/?name=image.png)**

**- EPI's vinculados a Avaliação de Risco:**

Acesse **PPRA/PGR** | **Reconhecimento e Avaliação de Risco** | **Edite a Avaliação vinculado ao Risco do funcionário** | **Guia EPI/EPC**

**![](https://totvssuporte.zendesk.com/attachments/token/PBWbZGWhvfwNU9YpeKDRpb2tY/?name=image.png)**

**2 -**Caso o parâmetro esteja desmarcado, o sistema considerará os equipamentos que foram vinculados ao **Risco** e **emprestados** ao Funcionário, ou seja, aqueles que não possuem a 'Data de Devolução' preenchida. Dessa forma, valide no anexo de EPIs se o equipamento vinculado ao Risco foi fornecido ao Funcionário. Caso não tenha, deverão emprestá-lo com uma data que compreenda o período da avaliação de risco através do **assistente de fornecimento automático**.  
  
[RH - RM - SMT - Fornecimento/Devolução EPIs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008882492-RH-RM-SMT-Fornecimento-Devolu%C3%A7%C3%A3o-EPIs?source=search)

![](https://totvssuporte.zendesk.com/attachments/token/ZWB268aNH2KzhYVNMkyb1qmUI/?name=image.png)

**Importante**- Deve validar no cadastro dos Lotes se todos os campos estão devidamente preenchidos e com as datas válidas, conforme informado acima.

- Caso o campo 'Filial' no cadastro do Lote estiver preenchido, é necessário que seja a filial que abrange a função do funcionário que está com o erro.

**Saiba Mais**Para maiores informações, acesse:

[RH - RM - SMT - Gerar o evento S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007674022-RH-RM-SMT-Gerar-o-evento-S-2240-Condi%C3%A7%C3%B5es-Ambientais-do-Trabalho-Fatores-de-Risco)

[RH - RM - SMT - Dúvidas frequentes sobre a geração dos eventos de SST para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414423920535-RH-RM-SMT-D%C3%BAvidas-frequentes-sobre-a-gera%C3%A7%C3%A3o-dos-eventos-de-SST-para-o-eSocial)
