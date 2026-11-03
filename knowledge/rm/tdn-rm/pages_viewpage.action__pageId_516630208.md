---
content_hash: a2ffd8b65dee0e10eff80b5dacb6da1a9d3db58b9bf51132f302519a118ff776
fetched_at: '2026-06-29T00:10:27.638740+00:00'
page_id: '516630208'
product: rm
source: tdn-rm
title: Mensagens Automáticas CIH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516630208
version: 2
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O envio de mensagens poderá ocorrer de duas formas:

Envio de e-mail automático.

Através de mensagem na tela do sistema.

Para cada grupo de usuários poderá ser definido qual o formato de apresentação deste alerta.   
Com esta implementação a solução passa a monitorar os seguintes eventos, cada um deles gerando uma mensagem distinta aos usuários:

* **Isolamento de germe multirresistente:** ao integrar (importar) um germe multirresistente no sistema será enviada uma mensagem (via sistema ou via e-mail) para o usuário que estiver cadastrado, informando que determinado paciente está com: "Isolamento de germe multirresistente".
* **Interrupção de antibiótico:** o usuário cadastra no sistema o tempo de tratamento das diversas topografias de infecção, e configurado o envio deste tipo de mensagem, o sistema enviará mensagens de acordo com o tempo de uso do antibiótico, informando aos destinatários que deve ser feita a interrupção do tratamento antimicrobiano, em conformidade com os protocolos de tratamento da instituição.
* **Possível reinternação por infecção hospitalar:** logo após a reinternação de um paciente uma mensagem de "Possível reinternação por IH" será gerada caso esta ocorra até 30 dias após a alta. Se o paciente tiver sido submetido a alguma cirurgia com implante de prótese, o alerta será enviado em período de até um ano após a alta.
* **Reinternação de paciente com bactéria multirresistente:** Será exibida a mensagem quando houver reinternação de um paciente que tenha tido isolamento de germe multirresistente em internação prévia (até 6 meses).
* **Crescimento bacteriano em espécime clínico crítico:** o usuário receberá esta mensagem quando houver crescimento de qualquer patógeno em materiais como sangue.

É importante ressaltar que para cada tipo de mensagem, deve ser informado qual destinatário e o tipo de envio (e-mail ou via sistema). Pode-se parametrizar o intervalo de tempo para o reenvio de uma mesma mensagem, via sistema, até que o destinatário tenha ciência.   
Há a interface de configuração de uma das mensagens de monitoramento. A configuração da mensagem pode ser customizada pelo cliente e neste sentido podemos estruturá-la com modificações no título e texto que compõem o corpo da mensagem. Neste texto, podemos inserir os parâmetros pré-estabelecidos para identificação do paciente e do atendimento relacionado, estes dados são recuperados do banco de dados no processo de envio.

## **02. EXEMPLO DE UTILIZAÇÃO**

Saúde > controle de infecção hospitalar  > utilitários > configura mensagens

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão | 1. No **Controle de Infecção Hospitalar** acesse **Utilitários/Configura Mensagens**. 2. Marque o tipo de mensagem e clique em **Editar**. 3. Será exibida a tela para edição, nela clique na guia **Destinatários**. 4. Clique em **Incluir**. 5. Será exibida tela para configuração, nela marque se a mensagem será envia via e-mail ou sistema (tela). 6. Preencha a informação de Filtro e clique em **OK**. |

## **04. TABELAS UTILIZADAS**
