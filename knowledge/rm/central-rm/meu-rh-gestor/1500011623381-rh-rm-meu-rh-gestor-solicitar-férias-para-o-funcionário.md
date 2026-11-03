---
article_id: 1500011623381
category: Meu RH - Gestor
content_hash: 50b065f8eb2784e8e3ea639ee85a0cc90171564820f935a1a4b296b23f9a0061
fetched_at: '2026-06-28T22:47:32.422039+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH- Gestor Solicitar Férias para o Funcionário
type: support-article
updated_at: '2024-11-01T16:12:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011623381-RH-RM-Meu-RH-Gestor-Solicitar-F%C3%A9rias-para-o-Funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22217162562711) Tempo aproximado para leitura: 00:03:08 min**  
**Dúvida**

Como habilitar permissão para o Chefe e Supervisor solicitar férias para o funcionário?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir do release 12.1.27  
  
**Solução**

Para que o gestor consiga solicitar  férias para o funcionário deve ser liberada  permissões nos seguintes itens:

  Portal RH (Portal) -> Equipe -> Subordinados -> Marcar Férias -> Marcação de Férias: Excluir -> Salvar - Marcar Férias -> Consulta Férias

 Para liberar a permissão deve acessar o  modulo Serviços Globais, menu Segurança e acesse a opção Perfis, selecione o  perfil do gestor e libere as permissões conforme  abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22217685932567)

No Grupo de quiosque do gestor possui 2 flags para ser parametrizadas :

**Chefe/Supervisores pode enviar direto para o cadastro do subordinados :**

 Caso a flag esteja habilitada, quando o Chefe/supervisor marcar as férias para o funcionário, as férias ficaram como marcadas. Com a flag desabilitada após marcação das férias pelo gestor a mesma irá para aprovação do DP.

**Supervisor pode programar férias:**

Caso a flag esteja desabilitada, Supervisor ficará impossibilitado de marcar férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27491992573975)

No meu RH para solicitar as férias para o funcionário deve acessar o menu Gestão de time | selecionar o funcionário e abrir a opção férias.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018716762)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018983741)

**Saiba Mais**

**[CLIQUE AQUI para saber sobre Gestão de Time](https://tdn.totvs.com/pages/viewpage.action?pageId=516621760)**

**[CLIQUE AQUI para saber sobre Utilização Chefe e Supervisor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006127202-RH-RM-Meu-RH-Utiliza%C3%A7%C3%A3o-Chefe-e-Supervisor-)**
