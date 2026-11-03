---
article_id: 360020220871
category: GPE - eSocial - Não Periódicos
content_hash: 89923df2067bd8f60ef5bcc6c0eef36594f8aa806fe238d7d80adba9e5709405
fetched_at: '2026-06-28T22:45:05.915027+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2300 - Como integrar o evento nos casos
  em que ele é Opcional
type: support-article
updated_at: '2026-06-16T13:45:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020220871-RH-Linha-Protheus-GPE-eSocial-S-2300-Como-integrar-o-evento-nos-casos-em-que-ele-%C3%A9-Opcional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35014642000919) Tempo aproximado para leitura: **00:03:00** min  
  
**Dúvida**Como integrar o evento nos casos em que ele é Opcional?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O **[Manual de orientações do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-04-2025.pdf),** na parte em que discorre sobre o evento **S-2300,** informa todos os código de categoria eSocial que **são obrigados** a enviar a informação, porém para os demais códigos de categoria eSocial de Trabalhadores Sem Vínculo ele informa que o evento **S-2300** é **OPCIONAL**, ou seja, não é obrigatório.  
  
Foi criado o parâmetro **MV\_NTSV**, você terá que remover dele a categoria do eSocial do Trabalhador que deseja enviar o evento S-2300, ou seja, ele define quais categorias do eSocial você **não** deseja gerar o evento S-2300. Em outras palavras, o funcionário com a categoria que estiver inserida no parâmetro **não** será enviado ao TAF.  
  
Por padrão o parâmetro **MV\_NTSV** vem com o conteúdo "**701/711/712/741**".  
  
Segue trecho do MOS leiaute S-1.3 a partir da página 241:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35014609986583)  
  
Para os **Trabalhadores Sem Vínculo SEM o evento S-2300** o Sistema envia ao **TAF** as informações complementares através do evento **S-1200**, porém o cadastro desse Trabalhador precisa ter um mínimo de informações exigidas pelo SIGAGPE e outro mínimo para atender as demandas do leiaute do **eSocial**, por exemplo os campos: Matricula, Nome, Sexo, Data de Nascimento, Centro de Custo, Categoria do Funcionário, Situação Folha, Cod. Processo, Cod. Função, Função, CBO, Tipo Pgto, Cat. SEFIP, CAT eSocial, Ocorrência, CPF e PIS.  
  
Para limitar a quantidade de campos exigidas no momento do cadastro o usuário deve utilizar a rotina de **Contribuinte Individual** do **GPE**, selecionar a opção **Outras Ações** e em seguida **Selec. Campos**.  
  
No **[Manual de orientações do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-04-2025.pdf)**, o item **'11.1 - Trabalhadores não incluídos no RET'** devem obrigatoriamente ter suas informações preenchidas no XML S-1200 no grupo [infoComplem]: **nome, data de nascimento etc** e no grupo [InfoComplCont]: **CBO, natureza da atividade** etc, quando do envio do evento S-2300 de identificação deste trabalhador que não está no RET.  
  
Para quem deseja enviar o evento **S-2300** para categorias do eSocial em que o evento é **OPCIONAL** será necessário retirar essa categoria do parâmetro **MV\_NTSV** e preencher todo o cadastro do trabalhador no SIGAGPE com as informações exigidas pelo leiaute do eSocial, o que seria basicamente todo o cadastro de Trabalhadores do SIGAGPE. Caso esteja com o parâmetro **MV\_RHTAF** igual a **.T.**, assim que gravar o registro no SIGAGPE o Sistema enviará o evento **S-2300** ao TAF. Nesses casos as informações complementares não podem ser informadas através dos eventos **S-1200**.  
  
**Artigo relacionados**

[RH - Linha Protheus - GPE - eSocial - S-2300 - Como gerar trabalhador autônomo (trabalhador sem vinculo) no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013341771-RH-Linha-Protheus-GPE-eSocial-S-2300-Como-gerar-trabalhador-aut%C3%B4nomo-trabalhador-sem-vinculo-no-TAF?source=search)   
[Boletim Técnico parâmetro MV\_NTSC](http://tdn.totvs.com/pages/releaseview.action?pageId=458753479)  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Documentações Técnicas do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
