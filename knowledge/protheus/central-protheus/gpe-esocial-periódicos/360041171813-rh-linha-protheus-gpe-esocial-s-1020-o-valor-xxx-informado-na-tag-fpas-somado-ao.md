---
article_id: 360041171813
category: GPE - eSocial - Periódicos
content_hash: 1bfb647260f108ef8ad15e82229474d1d8abad7c4e51feb897ca37bbbd52c0b8
fetched_at: '2026-06-28T22:45:07.633528+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1020 - O valor 'XXX' informado na tag
  fpas somado ao valor 'XXXX' informado na tag codTerceiros é uma chave composta e
  sua combinação não corresponde a nenhum registro do cadastro na base de dados
type: support-article
updated_at: '2025-07-17T14:22:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041171813-RH-Linha-Protheus-GPE-eSocial-S-1020-O-valor-XXX-informado-na-tag-fpas-somado-ao-valor-XXXX-informado-na-tag-codTerceiros-%C3%A9-uma-chave-composta-e-sua-combina%C3%A7%C3%A3o-n%C3%A3o-corresponde-a-nenhum-registro-do-cadastro-na-base-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33533475881751) Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**O valor 'XXX' informado na tag **fpas** somado ao valor 'XXXX' informado na tag **codTerceiros** é uma chave composta e sua combinação não corresponde a nenhum registro do cadastro na base de dados  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A causa é devido o Código de FPAS estar incorreto ou devido não ser condizente ao Código de Terceiros previsto no leiaute do eSocial vigente.  
Esse erro é apresentado no momento da integração do GPE com o TAF através da rotina de Eventos Periódicos ou no momento de gravar o cálculo de uma rescisão.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054500033)  
  
**Solução**Verifique o **código do FPAS e seus Códigos de Terceiros definidos pelo leiaute do eSocial** e ajuste a informação no Protheus, depois é só reprocessar a integração do GPE com o TAF que deseja.  
  
O qual código utilizar deverá ser analisado internamente em cada Empresa, de acordo com as combinações previstas pelo eSocial.  
  
Segue um print da **Tabelas 04 - Códigos e Alíquotas de FPAS/Terceiros** do eSocial, nele demonstro somente o FPAS 515, mas há todos os previstos na legislação.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15506058454039)​**O FPAS pode ser preenchido no cadastro da Filial do Configurador (SIGACFG). Nele é possível digitar 4 (quatro) dígitos, porém isso ocorre para o Sistema tratar o legado, sendo assim, o preenchimento deve respeitar a forma e quantidade de caracteres apresentados no leiaute do eSocial.  
  
Por exemplo, se estiver preenchido como **515** funciona normal, mas se for preenchido **0515** acontecerá o erro indicado nesse artigo.![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053640994)  
  
Já o Código de Terceiros, ele é preenchido na tabela S038 do SIGAGPE.  
Caminho SIGAGPE: Atualizações > Definições de Cálculo > Manutenção de Tabelas  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054508773)  
  
No Protheus, os códigos definidos no leiaute do eSocial ficam nas tabelas autocontidas do TAF, ela é atualizada conforme alterações trazidas pelo Governo e execução do *Wizard* do TAF, mas você pode incluir uma combinação diferente, porém o evento pode ser rejeitado ao ser enviado ao Governo por não haver previsão no leiaute.  
  
![](https://totvssuporte.zendesk.com/attachments/token/LVnojkSA53crHct00mz9z5VYV/?name=inline-2065419523.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/Rgii8QT0VXjUGVi1aTHfrLf3f/?name=inline434537687.png)​  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053643074)  
  
Segue documento sobre uma das rejeições retornadas pelo RET (Governo):  
[MP - GPE - eSocial - S-1020 - Erro de retorno do RET 247 - Codigo de Terceiros incompativel com o FPAS informado.Acao Sugerida: Para classificacao tributaria igual a [01, 02, 03, 04], informar 0000. Nos demais casos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033938073)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
