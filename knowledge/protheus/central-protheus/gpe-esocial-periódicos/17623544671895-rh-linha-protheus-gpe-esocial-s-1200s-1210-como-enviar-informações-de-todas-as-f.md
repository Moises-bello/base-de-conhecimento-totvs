---
article_id: 17623544671895
category: GPE - eSocial - Periódicos
content_hash: 9d461f8bfd03f4bf2da11feca9123a4889948b5e131aefcd8d2dbf91ee1df63f
fetched_at: '2026-06-28T22:45:08.775830+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-1210 - Como enviar informações
  de todas as filiais e registros do trabalhador no mesmo evento
type: support-article
updated_at: '2025-07-22T18:52:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623544671895-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-enviar-informa%C3%A7%C3%B5es-de-todas-as-filiais-e-registros-do-trabalhador-no-mesmo-evento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17623506467095) Tempo aproximado para leitura: **00****:01:00 min** **Dúvida**Como enviar informações de todas as filiais e registros do trabalhador no mesmo evento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para geração do evento **S-1200/S-1210** dos trabalhadores que possui **recibos** em **diferentes vínculos e/ou filiais** diferentes abaixo da mesma raiz de CNPJ e dentro do **mesmo período**, é necessário realizar a configuração abaixo para que o sistema gere somente um evento com todas as informações.  
  
Acessar a rotina **GPEA300** no caminho: Atualizações > Definições de Calculo > Mnemônicos e verificar os seguintes mnemônicos:   
**P\_ESOCMV** :  Deve ficar com .T. em todas as filiais  
**P\_MULTV**: Deve ficar com .T. em todas as filiais  
  
Também é importante que na geração dos eventos periódicos **todas as filiais sejam selecionadas,** caso as informações estejam em filiais diferentes.  
  
Essa orientação é utilizada para atender uma das regras de validações do [leiaute](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-S-1.1/regras.html) vigente demonstrado na imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17623266252055)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
