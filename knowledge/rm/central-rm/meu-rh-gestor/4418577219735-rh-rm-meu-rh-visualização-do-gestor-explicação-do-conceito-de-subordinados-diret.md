---
article_id: 4418577219735
category: Meu RH - Gestor
content_hash: 1a61045fbf56cf6980e0c8861e6ea90aa7ae38c47f2ef7094909c5b183ec866e
fetched_at: '2026-06-28T22:47:32.381447+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Visualização do Gestor, explicação do conceito de subordinados
  diretos e indiretos
type: support-article
updated_at: '2026-06-15T15:28:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418577219735-RH-RM-Meu-RH-Visualiza%C3%A7%C3%A3o-do-Gestor-explica%C3%A7%C3%A3o-do-conceito-de-subordinados-diretos-e-indiretos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22209634299159) Tempo aproximado para leitura: 00:04:20 min**

**Dúvida**  
Quais são as diferenças de subordinados diretos e indiretos no Meu RH?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões

**Solução**

As funcionalidades **Gestão de Férias** e **Minha Equipe** no Meu RH utiliza o conceito de subordinados diretos e indiretos para listar os colaboradores. Por padrão, ao acessar a tela pela primeira vez, são exibidos apenas os subordinados diretos. Para visualizar os subordinados indiretos, é necessário ativar o filtro "**Ver todos os colaboradores**" ou "**Ver colaboradores Indiretos"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310658086039)

Os subordinados podem estar associados a mais de um chefe ou supervisor. Contudo, apenas um deles será considerado o superior direto, enquanto os demais serão classificados como superiores indiretos. É possível consultar no Perfil do Meu RH qual gestor está sendo considerado como direto através do campo superior:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310658089751)

Os superiores diretos e indiretos possuem o mesmo nível de permissões gerenciais. Ambos recebem notificações de aprovações (como férias, batidas de ponto, abonos, entre outros) e podem realizar aprovações ou reprovações sem qualquer restrição.

#### Regras para Definição do Superior Direto

1. **Chefe com menor número de chapa:**

   Quando há mais de um chefe cadastrado na mesma seção do subordinado, o gestor com a **menor chapa** será considerado o superior direto. Exemplo: Na seção **01.03**, há dois chefes cadastrados:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310658092823)  
     
   **Alessandra** (Chapa 00005) será a **superior direta**.  
   **Marcelo** (Chapa 00011) será o **superior indireto** dos colaboradores desta seção.
2. **Supervisor possui prioridade sobre o chefe:**

   Se o colaborador possuir código de equipe em seu cadastro de funcionário, o supervisor desta equipe será considerado o superior direto, pois o supervisor tem prioridade sobre o cadastro de chefe. Exemplo: na seção **01.03**, há dois chefes e um supervisor:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310682135959)  
     
   **Ana Luiza** (Chapa 00012), como supervisora, será a **superior direta** dos colaboradores que possuem o código dessa equipe no cadastro de funcionário.  
     
   Colaboradores sem o código de equipe terão:   
   **Alessandra** (Chapa 00005) como superior direta.  
   **Marcelo** (Chapa 00011) como superior indireto.   
     
   Caso exista mais de um supervisor cadastrado para a mesma equipe na seção, será considerado como direto o supervisor que possuir a menor chapa.

**Saiba mais**  
[Meu RH - Gestão de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=285646619)  
[MEU RH - Gestão do Time](https://tdn.totvs.com/pages/viewpage.action?pageId=516621760)
