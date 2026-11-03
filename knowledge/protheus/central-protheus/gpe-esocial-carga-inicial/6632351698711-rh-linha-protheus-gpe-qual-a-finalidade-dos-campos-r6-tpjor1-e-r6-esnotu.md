---
article_id: 6632351698711
category: GPE - eSocial - Carga Inicial
content_hash: e7bd9ca42b1d2ebc3356f9725068a926e0cdd8e0a6820f48e0d7316faf2c4808
fetched_at: '2026-06-28T22:45:03.362328+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - Qual a finalidade dos campos R6_TPJOR1 e R6_ESNOTU
type: support-article
updated_at: '2025-04-02T12:50:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6632351698711-RH-Linha-Protheus-GPE-Qual-a-finalidade-dos-campos-R6-TPJOR1-e-R6-ESNOTU
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19452137030935)**Tempo aproximado para leitura: 00**:02:00 min** **Dúvida**Qual a finalidade dos campos R6\_TPJOR1 e R6\_ESNOTU?Exemplos de erros gerados:  
- Erro na validação do campo 'tpJornada': Valores válidos: 2,3,4,5,6,7,9.  
- Tipo de jornada no turno de horas escolhido é invalido, favor verificar o campo R6\_TPJOR1  
- Campo 'Turno Trab' não pode possuir campo "Jorn Sem Not" (R6\_ESNOTU) em branco.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Esses campos foram criados para atender as alterações do leiaute eSocial a partir da versão S-1.0em relação as *tag* **tpJornada** e **horNoturno.** Conforme demonstrado na imagem abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19452122170647)  
  
Para verificarmos o campo que atende a **tag tpJornada**, acesse **Atualizações - Ponto Eletrônico - Turno de Trabalho - aba Informações Ponto:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6632170377495)  
  
Para verificarmos o campo que atende a ***tag* horNoturno,** **acesse Atualizações - Ponto Eletrônico - Turno de Trabalho - aba Outros:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6632207502871)  
  
**Observação:**  
1 - A criação do campo ocorre com a aplicação dos pacotes contidos em nossa página entregas legais, inclusive atualização de dicionário ([eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw))  
2 - A demonstração do campo na rotina ocorre apenas a partir do leiaute S-1.1 conforme configuração dos parâmetros **MV\_VLESOC** e **MV\_TAFVLES**  
  
**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[Boletim técnico campo R6\_ESNOTU](https://tdn.totvs.com/display/public/PROT/12105948+DRHROTPRT-1247+DT+Cadastro+de+turno+no+leiaute+S-1.0+-+Campo+R6_ESNOTU)  
[Boletim técnico campo R6\_TPJOR1](https://tdn.totvs.com/pages/releaseview.action?pageId=639938616)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Próximos Treinamentos  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
