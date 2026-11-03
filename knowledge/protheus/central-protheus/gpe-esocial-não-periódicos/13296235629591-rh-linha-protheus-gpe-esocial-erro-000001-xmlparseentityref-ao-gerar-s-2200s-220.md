---
article_id: 13296235629591
category: GPE - eSocial - Não Periódicos
content_hash: f26819fd03ddcb2ddd164cf48d49a1e8f97b4e28fc2b7637cf4517bdce878dfe
fetched_at: '2026-06-28T22:45:04.372650+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - Erro 000001: xmlParseEntityRef ao gerar
  S-2200/S-2206/S-2300/S-2306'
type: support-article
updated_at: '2026-06-16T11:26:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13296235629591-RH-Linha-Protheus-GPE-eSocial-Erro-000001-xmlParseEntityRef-ao-gerar-S-2200-S-2206-S-2300-S-2306
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259077021463) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
*Erro 000001: xmlParseEntityRef: no name xmlParseMemory Failed Parse XML.* Esse erro pode ocorrer ao gerar os eventos S-2200, S-2206, S-2300, S-2306, entre outros.  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O erro é gerado quando em algum campo do cadastro existe um caractere especial. Como por exemplo, no cadastro de função em sua descrição, podemos ter o caractere &.  
  
Para caracteres o **esocial** possui uma **regra**:   
**1)** Pode conter exclusivamente caracteres presentes na lista abaixo, incluindo o espaço simples:  
! " # $ % & ' ( ) \* + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ \_ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ ¡ ¢ £ ¥ § © ª « ¬ ® ¯ ° ± ² ³ µ ¶ · ¹ º » À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ  
**2)** Não pode conter qualquer espaço no início ou no final.  
**3)** Não pode conter <tab>, <enter> e <espaço sem quebra visível>.  
  
O sistema está adequado aos caracteres, para **solucionar o erro** é necessário manter o ambiente **atualizado com o pacote de expedição continua**, contido na pagina [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
