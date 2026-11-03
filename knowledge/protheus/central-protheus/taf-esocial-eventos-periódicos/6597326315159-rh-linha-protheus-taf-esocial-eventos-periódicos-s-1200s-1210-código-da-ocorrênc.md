---
article_id: 6597326315159
category: TAF - eSocial - Eventos Periódicos
content_hash: e2cfa79e5334a851dd9f00780ab4950bdaf65cdf4d9d9ac3082843afb6f308d2
fetched_at: '2026-06-28T22:45:19.019067+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200/S-1210 -
  Código da Ocorrência: 106: Foi localizado no sistema um evento em duplicidade com
  o evento a ser enviado, mesmo Tipo de Inscrição, CPF do Trabalhador, Período de
  Apuração'
type: support-article
updated_at: '2026-06-25T11:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6597326315159-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-S-1210-C%C3%B3digo-da-Ocorr%C3%AAncia-106-Foi-localizado-no-sistema-um-evento-em-duplicidade-com-o-evento-a-ser-enviado-mesmo-Tipo-de-Inscri%C3%A7%C3%A3o-CPF-do-Trabalhador-Per%C3%ADodo-de-Apura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23701735818135) Tempo aproximado para leitura: **05:00:00 min** **Dúvida**No módulo do TAF, ao tentar realizar a transmissão do evento S-1200 (Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social) ou S-1210 (Pagamentos de Rendimentos do Trabalho) é apresentada a seguinte rejeição:  
 **Sequência: 000001 - Tipo: Erro - Código da ocorrência: 106   
Descrição: Foi localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, Numero de Inscrição, CPF do Trabalhador, Período de Apuração.  
  
Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**  
O eSocial identificou que já existe um evento enviado anteriormente que possui os mesmos dados, incluindo:

* Tipo de Inscrição (CNPJ, CPF, etc.)
* Número de Inscrição (CNPJ ou CPF do trabalhador)
* Período de Apuração

**Solução**

* **Cenário 1 - Evento indevido no eSocial:**

**1.** Acesse o portal eSocial e verifique se já existe o mesmo evento para o CPF e período em questão:  
  
**S-1200**: Folha de Pagamentos > Gestão de Folha:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820521334039)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820536923287)  
  
**S-1210**: Folha de Pagamentos > Gestão de Folha:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820536932375)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820521346199)  
  
**2.**Se já houver um evento no eSocial e o mesmo for indevido, realize a exclusão e tente transmitir novamente o evento com rejeição no TAF.

* **Cenário 2 - Múltiplos Vínculos:**

Para o eSocial só deve existir um único Evento Periódico para mesma raiz de CNPJ e mesmo CPF por período, ou seja, no exemplo narrado acima o Protheus deve considerar esse Trabalhador como Múltiplos Vínculos e gerar um único evento S-1200 aglutinando as informações da Filial 01 e 02.  
  
Para que o Evento Periódico de um Trabalhador seja gerado como Múltiplos Vínculos é necessário realizar as parametrizações e validações da documentação disponível no link abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar funcionários com múltiplos vínculos no evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013550551-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-no-evento-S-1200)  
  
**Importante validar os mnemônicos P\_ESOCMV e P\_MULTV.**Caminho: SIGAGPE > Atualizações > Definições Cálculo > Mnemônicos:![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820536939415)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820521353367)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820521355927)  
  
Segue abaixo um exemplo de geração do XML do evento S-1200 de Múltiplos Vínculos com remuneração em três Filiais de mesma raiz de CNPJ:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26820521360279)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
