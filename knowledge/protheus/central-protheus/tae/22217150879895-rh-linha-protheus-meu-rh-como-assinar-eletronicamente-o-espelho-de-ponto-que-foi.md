---
article_id: 22217150879895
category: TAE
content_hash: fd2178708f0341600e3342417a49f9a94815df5ab13e5560f42ed0ae54b642e4
fetched_at: '2026-06-28T22:44:30.131480+00:00'
product: protheus
section_id: 32238506930583
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como assinar eletronicamente o espelho de ponto
  que foi gerado pelo SIGAPON no Meu RH?
type: support-article
updated_at: '2025-09-16T17:12:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22217150879895-RH-Linha-Protheus-MEU-RH-Como-assinar-eletronicamente-o-espelho-de-ponto-que-foi-gerado-pelo-SIGAPON-no-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22222132125847) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como assinar eletronicamente o espelho de ponto que foi gerado pelo SIGAPON no Meu RH  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Ao realizar a solicitação de assinatura pelas funções de **geração do espelho de ponto dentro do ERP**, já está disponível a visualização e integração destes relatórios **pelo Meu RH**, as publicações podem ser realizadas diretamente pelo ERP Protheus, **seguidamente de sua assinatura pelo app Meu Rh.**

Para a integração **com o TAE,** obrigatoriamente, deverá ter configurado o **[protocolo SSL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133-RH-Linha-Protheus-MEU-RH-Como-configurar-o-SSL-HTTPS-para-o-MEU-RH)**, caso contrário, o TAE não aceitará as requisições vindas de um protocolo sem *SSL*.  
  
**Importante**: **Antes de realizar esse procedimento é necessário que a configuração de integração do TAE x Meu RH esteja feita conforme documentação abaixo**:  
[MEU RH - Integração da ferramenta TAE com o Meu RH para assinatura de documentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16786087683351-RH-Linha-Protheus-MEU-RH-Integra%C3%A7%C3%A3o-da-ferramenta-TAE-com-o-Meu-RH-para-assinatura-de-documentos)  
  
Após a configuração feita, deve-se habilitar o parâmetro [**MV\_MRHTAE**](https://tdn.totvs.com/pages/viewpage.action?pageId=741337177) = .T., esse parâmetro indica se os documentos (recibo de férias, aviso de férias e espelho de ponto), serão assinados **pelo TAE via Meu RH** (assinantes sem cadastro no TAE)

|  |
| --- |
| MV\_MRHTAE = .T. = Assinatura do aviso de férias, recibo de férias e espelho de ponto via Meu RH; |

|  |
| --- |
| MV\_MRHTAE = .F.= Assinatura do aviso de férias, recibo de férias e espelho de ponto via Plataforma TAE |

Acesse o módulo 16 - **SIGAPON >> Menu Relatórios >> Mensais >> Espelho de Ponto**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217150857239)

Ao acessar o espelho de ponto clique em parâmetros:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217182588823)

Selecione as opções que deseja gerar o relatório, exemplo matricula do funcionário, período do espelho que deseja gerar e deve se atentar a **pergunta "Integrar com TAE?"**, essa pergunta **igual a SIM**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217182590231)

Clique em OK e aguarde a geração do relatório, ao gerar o relatório será apresentado a informação que o **envio foi realizado com sucesso** e para qual *e-mail* foi feito o envio:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217182591767)

Acesse o TAE ([**https://totvssign.totvs.app/webapptotvssign/#/auth**](https://totvssign.totvs.app/webapptotvssign/#/auth)) e verifique se o espelho de ponto foi integrado:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217716143895)  
  
  
Ao acessar o Meu RH estará disponível o espelho de ponto para assinatura:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217716149911)

Espelho de ponto disponível para assinatura no Meu RH:![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217706829591)  
  
**Saiba Mais**  
**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**  
**[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
