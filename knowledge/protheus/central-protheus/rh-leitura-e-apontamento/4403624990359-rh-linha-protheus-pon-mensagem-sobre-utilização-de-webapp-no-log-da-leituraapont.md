---
article_id: 4403624990359
category: RH - Leitura e Apontamento
content_hash: f75ba3ed63ca813084c339e963e36baf82e0cb64bded8957f134d3162587330c
fetched_at: '2026-06-28T22:44:45.982696+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Mensagem sobre Utilização de WebApp no log da Leitura/Apontamento
type: support-article
updated_at: '2026-05-12T22:02:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403624990359-RH-Linha-Protheus-PON-Mensagem-sobre-Utiliza%C3%A7%C3%A3o-de-WebApp-no-log-da-Leitura-Apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40425788148247) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Mesmo não utilizando o *Smartclient Web*, no log da Leitura/Apontamento é exibida a mensagem: "Durante a utilização do *WebApp*, arquivos que estão fora da pasta Protheus\_Data não serão lidos. Por favor coloque o arquivo do relógio dentro da pasta Protheus\_Data e altere o cadastro do relógio ou execute a rotina pelo *Smartclient*."  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – A partir da versão 12.1.23  
  
**Causa**  
Esta mensagem é exibida quando existe uma **divergência** entre o **nome do arquivo TXT** salvo na pasta **X** o nome informado no **cadastro do relógio,** **ou** quando o usuário **deixa de usar** algum relógio de ponto, e para fins de histórico, **mantém o cadastro** no Protheus, porém, deixa o campo Nome Arquivo (P0\_ARQUIVO) em branco.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403616941975)  
  
**Solução**  
Para que a mensagem não seja exibida e não cause problemas no processo da Leitura/Apontamento, o usuário deve:  
**1.**Validar se o nome do arquivo TXT está exatamente igual ao informado no campo Nome Arquivo do cadastro do relógio. No exemplo da imagem abaixo o arquivo TESTE1.txt está no C: dentro da pasta Ponto.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407674610711)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403617023639)  
  
**2.** Caso exista um relógio de ponto que não é mais utilizado, o cadastro do Protheus deve ser mantido para fins de histórico, porém, orientamos que deixe o campo Nome Arquivo (P0\_RELOGIO) preenchido.  
  
Veja como realizar o [**Cadastro do Relógio de Ponto**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-RH-Linha-Protheus-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-de-Ponto)  
  
**3.** Verifique se o ambiente possui o [WebAgent](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent) instalado;

**4.** Verifique se a Porta do Webagent está habilitada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40425788150935)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40425739707415)  
  
**Saiba Mais**  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[WebAgent](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)
