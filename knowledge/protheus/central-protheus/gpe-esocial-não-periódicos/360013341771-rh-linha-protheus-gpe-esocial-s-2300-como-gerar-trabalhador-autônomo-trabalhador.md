---
article_id: 360013341771
category: GPE - eSocial - Não Periódicos
content_hash: 9d02b3c2719ca99dbb35517509a389ff0bd7bd0129a1fcb4133ff4031bb60c1c
fetched_at: '2026-06-28T22:45:05.909482+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2300 - Como gerar trabalhador autônomo
  (trabalhador sem vinculo) no TAF
type: support-article
updated_at: '2026-06-16T13:48:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013341771-RH-Linha-Protheus-GPE-eSocial-S-2300-Como-gerar-trabalhador-aut%C3%B4nomo-trabalhador-sem-vinculo-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25335356608791)**Tempo aproximado para leitura: **00:03:00  
  
Dúvida**Como gerar trabalhador **autônomo** (trabalhador sem vinculo) no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**De acordo com o MOS [(Manual de Orientação eSocial)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf), no tópico que trata o evento **S-2300**, os Trabalhadores sem vínculos devem ser gerados através do evento S-2300.  
  
Para o controle de envio dos autônomos para o **eSocial**, foi criado o parâmetro **MV\_NTSV**, o parâmetro irá definir quais categorias do **eSocial** não serão integrados com o TAF.  
  
Para maiores detalhes sobre o parâmetro acesse a o link: [RH Linha Protheus - GPE - eSocial - Novo controle de autônomos - Parâmetro MV\_NTSV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410718721687-RH-Linha-Protheus-GPE-eSocial-Novo-controle-de-aut%C3%B4nomos-Par%C3%A2metro-MV-NTSV).

Com isso existe duas possibilidades abaixo no sistema.

**1. Gerar Trabalhador Autônomo COM S-2300:**  
O trabalhador autônomo pode ser gerado no TAF através da execução da Carga Inicial (*GPEM023*), ou através do cadastro do Contribuinte Individual (*GPEA265*) quando o parâmetro **MV\_RHTAF**está com .T. e **MV\_FASESOC**está com 1 ou 2.  
[S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário - Início](http://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2300)  
  
No TAF os registros ficam gravados no **caminho:** Atualização > Eventos Esocial > Trabalhador > Cadastro Trabalhador.

**2. Gerar Trabalhador Autônomo SEM S-2300:**  
Gerado somente na execução do evento periódico **S-1200** (Folha de Pagamento) quando não existe **S-2300** no TAF.  
  
Também deve existir o cálculo da folha no SIGAGPE referente ao mês executado na rotina eventos periódicos.  
  
No TAF são gravados os dados de Nome, CPF, Data de Nascimento, e PIS no **caminho:** Atualização > Eventos Esocial > Trabalhador > Trabalhador Autônomo.  
  
**Atenção:** Para o sistema gerar o S-1200 para os autônomos **sem S-2300** é obrigatório que os campos Nome, CPF, Data de Nascimento, Categoria eSocial, Função e CBO estejam preenchidos no cadastro do autônomo no SIGAGPE.  
  
**Artigos Relacionados:**

* [RH - Linha Protheus - GPE - eSocial - S-2300 - Como integrar o evento nos casos em que ele é Opcional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020220871-RH-Linha-Protheus-GPE-eSocial-S-2300-Como-integrar-o-evento-nos-casos-em-que-ele-%C3%A9-Opcional?source=search)
* [RH - Linha Protheus - GPE - eSocial - Saneamento de Base - Como consultar, configurar ou alterar os parâmetros do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25252443928855-RH-Linha-Protheus-GPE-eSocial-Saneamento-de-Base-Como-consultar-configurar-ou-alterar-os-par%C3%A2metros-do-Protheus)
* [S-1200 – Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-1200)

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
