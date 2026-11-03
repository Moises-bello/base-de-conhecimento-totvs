---
article_id: 4418236650903
category: Meu RH - Gestor
content_hash: d222c5df72e02d7c90006e1c16b0966475db6e60ba0b70256809d1327e88b46d
fetched_at: '2026-06-28T22:47:32.386650+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Como o Chefe ou Supervisor visualiza o espelho de ponto
  do time
type: support-article
updated_at: '2026-06-01T18:41:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418236650903-RH-RM-Meu-RH-Como-o-Chefe-ou-Supervisor-visualiza-o-espelho-de-ponto-do-time
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22209738089879) Tempo aproximado para leitura: **00:02:50 min**  
  
**Dúvida**  
Quais as permissões necessárias para Chefe ou Supervisor visualizar o espelho de ponto dos seu time?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.29  
  
**Solução**  
Para que o Chefe ou Supervisor tenha a visão do espelho de ponto de seus subordinados ele deve ter as permissões liberadas em seu perfil;

Acesse a MDI **Serviços Globais | Segurança | Perfis | Sistema: Automação de Ponto**

As permissões que permitem a visualização do espelho de ponto dos subordinados são:

- Em **Equipe | Subordinados** devem ser permitido o menu **Visualizar Ponto**

- Para visualizar as batidas por Geolocalização em **Equipe | Portaria 373/2011** deve ser permitido o menu **Gestor: Visualizar batidas de subordinados**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22209903626007)

Ao acessar o Meu RH após liberar as permissões será apresentado a opção em **Minha Equipe | Ponto.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22209943978135)

Também ficará disponível a visualização das Batidas Remotas onde serão apresentadas as batidas por Geolocalização.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22209903644823)

**Importante**  
O relatório padrão disponibilizado pela TOTVS não contempla a geração da todos subordinados de um gestor ou geração em lote, uma vez que a funcionalidade atual do Meu RH realiza a geração do documento de forma individual para cada colaborador.

Para atender ao cenário desejado, será necessário desenvolver um relatório customizado com a finalidade específica da empresa, permitindo sua disponibilização e execução por meio do menu **Relatórios**.

Ressaltamos que o Suporte Padrão não realiza a criação, manutenção ou ajustes em relatórios customizados. Caso necessário, esse serviço pode ser contratado junto à Consultoria TOTVS.

Além disso, para que um relatório possa ser executado pelo portal Meu RH, ele deve seguir a estrutura e os padrões exigidos pela plataforma. Relatórios que não atendam a esses requisitos não serão disponibilizados para geração no portal.

A documentação abaixo apresenta os critérios necessários para desenvolvimento de relatórios compatíveis com o Meu RH, bem como um modelo básico que pode ser utilizado como referência na criação do relatório customizado:  
[**RH - RM - Meu RH - Como utilizar relatórios customizados do tipo "Meus dados" ou "Dados da minha equipe" no Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40770198640791)

**Saiba mais:**  
[**Meu RH - Ponto**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000861782-Meu-RH-Ponto)[**Como habilitar o menu ponto?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009131801-RH-RM-Meu-RH-Como-Habilitar-o-Menu-Ponto)
