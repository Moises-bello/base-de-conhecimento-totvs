---
article_id: 360035242153
category: GPE - eSocial - Não Periódicos
content_hash: f997754a5f6d8c8dd74a530cd9e77da7da3a528a4eddc2c3595715b3b281f59c
fetched_at: '2026-06-28T22:45:04.452635+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Ao transmitir o evento ao RET
  (Governo) é retornada a mensagem cnpjSindCategProf não preenchido"
type: support-article
updated_at: '2026-06-16T13:35:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035242153-RH-Linha-Protheus-GPE-eSocial-S-2200-Ao-transmitir-o-evento-ao-RET-Governo-%C3%A9-retornada-a-mensagem-cnpjSindCategProf-n%C3%A3o-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262163016087) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Ao transmitir o evento ao RET (Governo) é retornada a mensagem "**cnpjSindCategProf** não preenchido"  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
O motivo da inconsistência é devido o evento S-2200 não conter a informação do CNPJ do Sindicato de classe do Trabalhador.  
  
**Solução**  
Para solucionar essa inconsistência acesse o cadastro do Trabalhador e verifique na aba **Funcionais** se o Trabalhador está vinculado a um Sindicato, se não estiver, será necessário incluir tal informação e ao gravar o registro será enviado uma retificação do evento S-2200.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045979613)  
  
Caso o Trabalhador já esteja vinculado a um Sindicato você deverá verificar o cadastro do Sindicato e se atentar ao preenchimento do CNPJ do Sindicato, para isso acesse as opções do Menu do SIGAGPE: Atualizações > Cadastro > Sindicatos.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045121434)  
  
Para evitar que o cadastro de um Trabalhador seja gravado com ausência de informações obrigatórias para o eSocial utilize o parâmetro **MV\_EFDAVIS**.  
Caso o parâmetro **MV\_RHTAF** esteja como .T. e **MV\_EFDAVIS** esteja como "1", o sistema exibe a mensagem de inconsistência e bloqueia o cadastro até que todos os campos obrigatórios para o **eSocial** sejam preenchidos, para mais informações, [**clique aqui**](https://tdn.totvs.com/pages/viewpage.action?pageId=286499282).  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
