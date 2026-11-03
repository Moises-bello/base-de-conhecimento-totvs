---
article_id: 35543246373655
category: MIDDLEWARE eSocial
content_hash: b395854d4a1728219f27f708f053cfe274ff50cf9d09aef72772c1c445644a59
fetched_at: '2026-06-28T22:43:04.935432+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Middleware - Erro 401 Não Autorizado
type: support-article
updated_at: '2026-06-17T19:18:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35543246373655-RH-Linha-Protheus-TAF-eSocial-Middleware-Erro-401-N%C3%A3o-Autorizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35543232737815) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Ocorrência**  
Ao realizar o envio dos eventos no Middleware, apresenta o erro - Ocorreu erro que impediu a execução do processo. System.AggregateException: One or more errors occurred. ---> RM.Lib.RMSValidateException: Requisição inválida.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões.  
  
**Causa**  
Esse erro ocorre ao migrar o TAF para a release 12.1.2410, onde é obrigatório definir uma senha para o usuário admin.  
  
**Solução**  
1. Acesse o SIGACFG (Configurador) - [RH - Linha Protheus - TAF - eSocial - Configurador - Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413-RH-Linha-Protheus-TAF-eSocial-Configurador-Como-acessar-o-configurador)

2. Dentro do Configurador, acesse o caminho: Usuario - Senhas - Usuarios

3. Clique em "Alterar" no usuário Administrador

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35543246363159)

4. Defina a senha no campo "senha" e confime

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35543246363415)

5. Para clientes RM, vá em: Configurações - Parametrizador - eSocial - Integração com Middleware e defina a senha e depois vá em "Avançar" e "Última Etapa" para salvar a senha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35543232738583)

Para clientes Datasul, vá em FP0560, na aba Conf Mid e altere conforme o print abaixo

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/40622869199639)

6. Teste o envio novamente

**Saiba Mais**

**Para saber mais consulte os links abaixo:**

[**eSocial | Protheus - Entregas Legais**](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[**MOS - Manual de Orientação eSocial**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[**Perguntas Frequentes site eSocial**](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

**Para conhecimento dos eventos futuros, acessa a nossa página**[**TOTVS Informa**](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "Eventos"**

**Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:**[**Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus)
