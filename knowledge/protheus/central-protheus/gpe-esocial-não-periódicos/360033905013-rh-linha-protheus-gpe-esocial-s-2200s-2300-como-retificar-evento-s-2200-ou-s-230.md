---
article_id: 360033905013
category: GPE - eSocial - Não Periódicos
content_hash: d3fceae1ccb619d20f89419d4c7140117cb50634a1fda751e6cdb076cf992efe
fetched_at: '2026-06-28T22:45:04.636331+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200/S-2300 - Como retificar evento
  S-2200 ou S-2300
type: support-article
updated_at: '2026-06-16T13:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033905013-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2300-Como-retificar-evento-S-2200-ou-S-2300
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26747301400983) Tempo aproximado para leitura: 01:00 min**  
  
**Dúvida**  
Como retificar evento S-2200 ou S-2300 enviado com informações indevidas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Após ajustar a informação enviada indevidamente, após ajuste no cadastro é necessário gerar o evento de retificação. Para retificar essa informação foi disponibilizado no sistema 3 opções:  
  
**Opção 1:**  
No SIGAGPE você pode acessar a rotina de Carga Inicial e enviar um novo evento S-2200 ou S-2300 para esse Trabalhador com status de ativo, porém nos parâmetros do evento deverá preencher o campo Retificação igual a "SIM".  
  
Caminho SIGAGPE: *Miscelânea > eSocial > Carga Inicial*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26747301401751)​

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26747363052823)  
  
**Opção 2:**  
Ative o parâmetro **MV\_RETSOC**.   
Ao acessar a rotina de Cadastro de Funcionários, busque o registro desejado, selecione a opção Alterar e realize o ajuste devido.  
  
Caminho SIGAGPE: *Atualizações > Funcionários > Funcionários*  
Ao salvar o cadastro vai abrir uma mensagem de atenção, dizendo que foi alterado informações que devem ser enviadas ao governo, e pergunta se deseja gerar ou não um retificador do S-2200 ou S-2300.  
Para que seja gerado o evento S-2200 ou S-2300 de retificação, deve colocar SIM na pergunta abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26747363053975)  
  
Caso não possua o parâmetro, verifique o artigo abaixo:   
[Como criar o parâmetro MV\_RETSOC?](https://tdn.totvs.com/pages/releaseview.action?pageId=450143939)  
  
**Opção 3:**  
No SIGATAF você pode acessar a rotina de Cadastro do Trabalhador, filtrar o registro desejado e selecionar a opção Alterar, desta forma serão apresentadas algumas opções e você deverá selecionar a opção retificar.  
  
Caminho SIGATAF:​ *Atualizações > Eventos Esocial > Trabalhador > Cadastro Trabalhador*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26747363055511)​  
  
Você deverá apagar ou alterar as informações indesejadas do cadastro e gravar a Retificação, dessa forma ficará disponível no Painel do eSocial do TAF um evento S-2200 ou S-2300 de retificação para esse Trabalhador.  
  
**ATENÇÃO:** Caso você já tenha enviado eventos posteriores ao S-2200 ou S-2300 (o S-2205, o S-2206 ou S-2306), talvez  seja necessário excluir tais eventos para concluir a retificação, mas os riscos e impactos deverão ser analisados por seu departamento jurídico, e sugiro que confirme a necessidade direcionando um questionamento diretamente ao RET (Governo) através dos canais de comunicação disponíveis através do portal do eSocial.

* [Fale Conosco](https://www.gov.br/esocial/pt-br/canais_atendimento)
* [Central de Atendimento: 0800 730 0888](https://www.gov.br/esocial/pt-br/canais_atendimento)

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
