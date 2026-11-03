---
article_id: 360057637274
category: RH - Soluções para error.log
content_hash: 503b966640b2fb3a62edf3d625f5a086b001b39acb683bc0db66c6929c3fea35
fetched_at: '2026-06-28T22:44:08.816183+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar dicionário padrão em meu ambiente
type: support-article
updated_at: '2026-04-06T12:32:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057637274-RH-Linha-Protheus-GPE-Como-criar-dicion%C3%A1rio-padr%C3%A3o-em-meu-ambiente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16979547278615)** Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como criar dicionário padrão em meu ambiente?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para criar o dicionário no padrão do sistema, de forma atualizada, siga os passos abaixo:  
**1.** Baixe os arquivos de dicionários (completo e diferencial completo) disponíveis no Portal:  
  
**Release 12.1.2310:**  
[Dicionário completo](https://suporte.totvs.com/portal/p/10098/download#detail/1112210)   
[Dicionário diferencial](https://suporte.totvs.com/portal/p/10098/download#detail/1112208)  
  
**Release 12.1.2410:**  
[Dicionário completo](https://suporte.totvs.com/portal/p/10098/download#detail/1167447)  
[Dicionário diferencial](https://suporte.totvs.com/portal/p/10098/download#detail/1167445)  
  
**Release 12.1.2510:**  
[Dicionário completo](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1217199)  
[Dicionário Diferencial](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1217197)  
  
Em **Filtro de pacotes,** selecionar **Todos pacotes disponíveis.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31470034281239)**  
  
**2.**Coloque o conteúdo dos arquivos baixados no diretório ***systemload***da instalação do Protheus, substituindo todos os arquivos que já estiverem neste diretório;  
  
**3.**Acesse o módulo de **Configurador**, na rotina **Ambiente/Empresas** e crie uma nova **Empresa** ou **Grupo de Empresas**, de acordo com sua Gestão Corporativa;  
  
**4.** Acesse esta **nova empresa**, de preferência no Módulo de Configurador ou diretamente em um módulo, como SIGAGPE ou SIGAPON. Realizar este primeiro acesso como SIGAMDI ou SIGAADV não cria todas as tabelas necessárias, sendo necessário acessar algumas rotinas para carregar todas as tabelas;  
  
**5.** Quando a mensagem **Criação de Base** for apresentada, selecione a opção para criação **Com Registros Padrão.**  
  
**6.** Aguarde a **criação** de toda a empresa;  
  
**7.** Após a finalização da criação da empresa e seus dicionários, execute o processo de **UPDDISTR.**  
  
**8.** Verifique se o pacote de **Expedição Contínua do RH** é mais recente que o Dicionário Diferencial Completo do item 1 e, caso for, atualize também o Dicionário Diferencial da Expedição Contínua, após rodar os dicionários acima, colocando os arquivos no diretório ***systemload*****,** substituindo os que já existem e execute o **UPDDISTR** mais uma vez;  
  
**9.** Agora o **ambiente** (Dicionários) desta empresa **estará padrão** do sistema Protheus para sua versão, **atualizado** em todos os módulos e com a atualização mais recente dos Módulos de RH, sendo Gestão de Pessoal, Ponto Eletrônico, Cargos e Salários, Treinamento, Avaliação e Pesquisa de Desenvolvimento, Arquitetura Organizacional, Recrutamento e Seleção e Portais do Capital Humano, Participante e Meu RH.  
  
**Saiba mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
