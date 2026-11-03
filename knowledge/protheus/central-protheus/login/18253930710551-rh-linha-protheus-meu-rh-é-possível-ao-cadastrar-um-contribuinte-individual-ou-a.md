---
article_id: 18253930710551
category: LOGIN
content_hash: fe1806cfb8714250b31c67e56f7000d3e4506ac7451c483a1a39b96f0385203a
fetched_at: '2026-06-28T22:44:40.486450+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível ao cadastrar um contribuinte individual
  ou autônomo, relacionar como participante automaticamente?
type: support-article
updated_at: '2026-06-23T21:24:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18253930710551-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-ao-cadastrar-um-contribuinte-individual-ou-aut%C3%B4nomo-relacionar-como-participante-automaticamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18253891772951) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível ao cadastrar um contribuinte individual ou autônomo, relacionar como participante automaticamente?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Ao cadastrar um **Contribuinte Individual, ou Autônomo**, pela rotina específica do **módulo 07 - SIGAGPE**, é possível que esse cadastro seja automaticamente, levado ao **Cadastro de Participantes**, rotina APDA020.  
  
No Sistema Protheus, existe o parâmetro **MV\_AUTPART**.   
Este parâmetro existe para definir sobre a **Inclusão de Participante** a partir do **Cadastro de Autônomos**, e deve conter um dos valores abaixo de acordo com a necessidade de cada empresa:  
**1 = Pergunta se inclui.**  
**2 = Sempre inclui.**  
**3 = Nunca inclui.**  
  
Cadastro de Contribuinte Individual/Autônomo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18253485471767)  
  
Como o parâmetro por padrão tem o valor em branco, o sistema assume o valor 3 que no caso, **nunca inclui o registro na tabela RD0 (participantes).**  
  
Para alteração do parâmetro, acesso o Configurador, com o programa inicial **SIGACFG** e, na rotina **Ambiente > Cadastros > Parâmetros**, localize o **MV\_AUTPART** e edite, alterando para o conteúdo 1 ou 2, de acordo com a necessidade da Empresa.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18253293329047)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
