---
article_id: 22220915685399
category: TAE
content_hash: 0abfce814800ae38dae370cfb5766922ad857ea4459804ff0a66e25dc2f9d6e8
fetched_at: '2026-06-28T22:44:30.120421+00:00'
product: protheus
section_id: 32238506930583
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como assinar eletronicamente o aviso de férias
  que foi gerado pelo SIGAGPE no Meu RH?
type: support-article
updated_at: '2025-09-16T17:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22220915685399-RH-Linha-Protheus-MEU-RH-Como-assinar-eletronicamente-o-aviso-de-f%C3%A9rias-que-foi-gerado-pelo-SIGAGPE-no-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22222666485271) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como assinar eletronicamente o aviso de férias que foi gerado pelo SIGAGPE no Meu RH  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Ao realizar a solicitação de assinatura, pelas funções **de geração do aviso de férias e/ou recibo de férias** dentro do ERP, já está disponível a visualização e integração destes relatórios **pelo Meu RH**, as publicações podem ser realizadas diretamente pelo ERP Protheus, seguidamente de sua assinatura pelo App Meu RH.  
  
Para a integração **com o TAE,** obrigatoriamente deverá ter configurado o **[protocolo SSL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133-RH-Linha-Protheus-MEU-RH-Como-configurar-o-SSL-HTTPS-para-o-MEU-RH)**, caso contrário o TAE não aceitará as requisições vindas de um protocolo sem *SSL*.  
  
**Importante**: **Antes de realizar esse procedimento é necessário que a configuração de integração do TAE x Meu RH esteja feita conforme documentação abaixo**:  
[MEU RH - Integração da ferramenta TAE com o Meu RH para assinatura de documentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16786087683351-RH-Linha-Protheus-MEU-RH-Integra%C3%A7%C3%A3o-da-ferramenta-TAE-com-o-Meu-RH-para-assinatura-de-documentos)  
  
Após a configuração feita, deve-se habilitar o parâmetro [**MV\_MRHTAE**](https://tdn.totvs.com/pages/viewpage.action?pageId=741337177) = .T., esse parâmetro indica se os documentos (recibo de férias, aviso de férias e espelho de ponto) **serão assinados pelo TAE via Meu RH** (assinantes sem cadastro no TAE):

|  |
| --- |
| MV\_MRHTAE = .T. = Assinatura do aviso de férias, recibo de férias e espelho de ponto via Meu RH; |

|  |
| --- |
| MV\_MRHTAE = .F.= Assinatura do aviso de férias, recibo de férias e espelho de ponto via Plataforma TAE |

Acesse o módulo 07 - **SIGAGPE >> Miscelânea >> Cálculos >> Férias:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220909673751)

Ao acessar a rotina de Cálculo de Férias clique em **Outras Ações >> Assinatura Eletrônica:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220909680407)

Clique em parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220909686039)

Selecione a integração com o TAE, **aviso de Férias e/ou Recibo de Férias:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220915627159)

Selecionar as opções que deseja gerar o relatório, exemplo matricula do funcionário, período das férias que deseja gerar e deve se atentar a **pergunta "Tipo de Relatório?"**, essa pergunta deve estar **igual a Integrar com TAE**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220915632407)

Clicar em OK e aguardar a geração do relatório, após, será apresentado a informação que **o envio foi realizado com sucesso** e para qual *e-mail* foi feito o envio.  
  
Acesse o TAE (<https://totvssign.totvs.app/webapptotvssign/#/auth>) e verificar se o **Aviso e/ou Recibo de Férias foram integrados:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220909703191)  
  
  
Ao acessar o Meu RH estará disponível o Recibo e Aviso de Férias:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220909713431)

Aviso de férias disponível para assinatura no Meu RH:![](https://centraldeatendimento.totvs.com/hc/article_attachments/22220915653655)  
  
**Saiba Mais**  
**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**  
**[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
