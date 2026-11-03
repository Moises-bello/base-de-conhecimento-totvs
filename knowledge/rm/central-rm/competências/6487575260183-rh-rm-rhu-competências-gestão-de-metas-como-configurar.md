---
article_id: 6487575260183
category: Competências
content_hash: a190192c284b521599746dcb244d15bb492e5375b16d3b0ffdfb08d26c99995e
fetched_at: '2026-06-28T22:47:20.230041+00:00'
product: rm
section_id: 1500000861322
source: central-rm
title: 'RH - RM - RHU - Competências - Gestão de Metas: Como configurar'
type: support-article
updated_at: '2026-02-27T14:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6487575260183-RH-RM-RHU-Compet%C3%AAncias-Gest%C3%A3o-de-Metas-Como-configurar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15868106398103) Tempo aproximado para leitura **00:05:00 min**  
  
**Dúvida**  
Quais são os passos para configurar a gestão de metas ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - A partir da 12.1.  
  
**Solução**

A Gestão de Metas tem como objetivo definir o caminho (metas) a ser cumprido pelos funcionários para se chegar a um objetivo.   
Para realizar a configuração, siga os passos abaixo:

1 - Acesse o menu **Acompanhamento > Gestão de Metas** e crie um novo registro, informando nome, tipo e o período da meta:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311371543)  
  
2 - **Meta** **Tipo Agrupadora**:   
  
A Meta Agrupadora funciona como uma "meta mestre" ou "meta pai". Sua finalidade é consolidar os resultados de diversas submetas (metas filhas) em um único indicador. O desempenho da meta agrupadora é calculado com base no peso (percentual) atribuído a cada meta que a compõe. Dessa forma esta meta não terá um valor de realização direto, mas sim um valor derivado de sua composição.  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686315058583)

- Aba '**Composição de Metas**':  
  
Nesta seção, é definido quais itens alimentarão a Meta Agrupadora. É possível vincular dois tipos de registros à composição:

* **Meta Valor:** Metas quantitativas diretas.
* **Meta Agrupadora:** Outras metas de grupo, permitindo a criação de subníveis.
* **Percentual:** Cada meta vinculada deve receber um valor numérico entre **0 e 100**.
* **Somatório:** O sistema monitora a soma de todos os percentuais. Caso o total ultrapasse **100%**, será emitido um **alerta de revisão** para o usuário.

Para garantir a integridade dos dados, existem regras de status para edição e vínculo:

* **Status da Meta Pai:** A composição só pode ser alterada se a meta agrupadora estiver como **"Em planejamento"** ou **"Suspenso / Replanejamento"**.
* **Status das Metas Filhas:** Somente metas que estejam nos status **"Em planejamento"** ou **"Suspenso / Replanejamento"** podem ser selecionadas para compor o grupo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311373847)

**Observação:** Caso **não tenha metas disponíveis** para vincular, pule para o **passo 3** e siga os passo de como cadastrar uma meta valor ou crie uma nova meta agrupadora, para que assim vincule em composição das metas.

- Aba '**Atribuições':**  
Define-se aqui quem são os responsáveis pela entrega e pela avaliação da meta.

**Avaliador (Quem avalia)**: Um funcionário específico OU um avaliador externo.  
      **Avaliados (Quem entrega)**: Deve-se preencher **apenas uma** das opções abaixo:

* Uma Seção;
* Uma Equipe;
* Um Funcionário;
* Um Externo.

Assim como na composição, as atribuições de responsáveis só podem ser modificadas se a meta estiver nos status de **Planejamento ou Suspenso/Replanejamento.**  
  
3 **-Meta Tipo Valor:**   
Na aba '**Configuração'**, define-se como o sistema validará o alcance do objetivo e como os dados serão processados.

Existem duas formas de validar o cumprimento:

* **Valor de Referência:** Utilizado para metas diretas com um ponto de corte fixo.

  + **Valor referência:** Informe o número base (ex: 1.000,00).
  + **Cumprimento da meta:** Defina se o sucesso ocorre **Acima** ou **Abaixo** do valor de referência.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311374871)

* **Faixa de Valores:** Utilizado para cenários onde o desempenho varia conforme intervalos atingidos. Habilita uma aba específica para cadastro.

  + **Operadores:** Utilize `<`, `<=`, `>`, `>=` e `=` para cobrir todos os resultados possíveis.
  + **Meta Cumprida:** Marque o campo "Meta Cumprida quando estiver nesta faixa" para indicar o sucesso.
  + **Fator Multiplicador:** Define o índice para o cálculo da **Remuneração Variável** (conforme regras de Valorização).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686315066007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311377815)

##### - **Forma de avaliação:** Define como o sistema interpretará múltiplos lançamentos de resultados:

* **Somatório dos lançamentos:** Soma todos os valores registrados no período.
* **Último lançamento:** Considera apenas o valor mais recente inserido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686315066647)

**- Opções:**

Configurações que regem a interação do colaborador com a meta:

* **Avaliado visualiza meta:** Permite a consulta via portal.
* **Exige aceite dos avaliados:** O avaliador pode solicitar concordância formal (dispara e-mail de pendência).
* **Avaliado pode lançar resultado:** Permite que o próprio funcionário registre seu progresso.
* **Lançamento exige aprovação:** O registro fica pendente até o avaliador validar.
* **Pode solicitar aprovação:** Envia e-mail ao avaliador notificando a pendência de aprovação.
* **Envio automático de e-mail:** Notifica o avaliador imediatamente após qualquer lançamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311379479)

Na aba '**Atribuições'** é definido os atores envolvidos na meta (Alterações aqui só são permitidas nos status **"Em Planejamento" ou "Suspenso/Replanejamento"**).

* **Avaliador:** Deve-se preencher **apenas uma** opção (um funcionário OU um externo).
* **Avaliados:** Deve-se preencher **apenas uma** opção (uma Seção, Equipe, Funcionário OU Externo).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686315070103)

⚠️**Importante para a Integridade dos Dados:**

* **Exclusão e Alteração:** Uma meta só pode ser excluída ou ter atribuição/composição alterada se estiver no status **"Planejamento"**.
* **Mudança de Tipo:** Se uma Meta Agrupadora já for "pai" de outras metas, ela **não poderá** ser convertida para Meta Valor.
* O resultado da meta refere-se à meta em si, e não individualmente aos membros da atribuição. A apuração é global para o objetivo definido.

4 - **Vínculo de Requisitos e Competências**

As metas podem ser utilizadas como ferramentas de capacitação. Ao concluir uma meta, o sistema pode disponibilizar automaticamente requisitos de acesso ou competências ao funcionário.

A associação não é feita diretamente no cadastro da meta, mas sim através do menu **Processos**:

* **Para Requisitos:** Processos | Vincular/Desvincular Requisitos de Acesso a Metas.
* **Para Competências:** Processos | Vincular/Desvincular Competências a Metas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311383831)

Para verificar o que está associado a cada objetivo, selecione a meta e utilize o menu **Anexos**:

* Anexos | Requisitos de Acesso Vinculados
* Anexos | Competências Vinculadas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686315074967)  
  
5- **Ativação do Ciclo de Metas (Mudança de Status)**

Após concluir o cadastro da Meta Agrupadora, das Metas de Valor e realizar os devidos vínculos de composição, as metas precisam ser "abertas" para que o trabalho comece.

##### 

##### **Processo de Abertura**

1. Selecione as metas desejadas.
2. Acesse: **Processos | Trocar status | Abrir/Replanejar Metas**.
3. Uma vez abertas, as metas ficam disponíveis para lançamentos tanto no **ERP (RM)** quanto no **Totvs Portal**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311388951)

**Dica de Auditoria:** Na Meta de Valor, a aba Lançamentos funciona como um histórico centralizado. Nela, você pode visualizar todos os registros feitos manualmente, via Portal ou por processos automatizados do sistema.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38686311390359)  
  
6 - **Lançamento de Resultados (Metas Tipo Valor)**

O registro do progresso é realizado exclusivamente em metas que já foram planejadas e ativadas.

##### 

##### **Como realizar o lançamento:**

1. Acesse o menu **Acompanhamento | Gestão de Metas**.
2. Selecione uma meta do tipo **Valor**.
3. Vá até a aba **Lançamentos**.

##### **Regras de Preenchimento**

* **Data de Alteração:** O sistema sugere a data atual por padrão. **Importante:** Não é permitido inserir uma data futura (maior que a data de hoje).
* **Conteúdo do Registro:** É possível preencher apenas o campo **"Valor"**, apenas o **"Comentário"**, ou ambos simultaneamente para detalhar o progresso.
* **Restrição de Status:** A inclusão, exclusão ou edição de lançamentos só é permitida se a meta estiver com o status **"Aberta"**.

**Saiba Mais:**  
Para maiores informações, acesse:

- [Gestão de Metas](https://tdn.totvs.com/pages/viewpage.action?pageId=452719260)

- [Vincular/Desvincular Requisitos de Acesso e Metas](https://tdn.totvs.com/pages/releaseview.action?pageId=452718865)

[- Cadastro de Targets](https://tdn.totvs.com/display/LRM/Cadastro+de+Targets)
