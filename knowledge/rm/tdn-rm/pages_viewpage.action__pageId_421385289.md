---
content_hash: 6caaad33cf3c07ab6d0f62bb3a7463db30a9b4f34f168dabcdc09a0f8a733870
fetched_at: '2026-06-29T00:09:14.872301+00:00'
page_id: '421385289'
product: rm
source: tdn-rm
title: Enviar Apontamentos para o Manutenção de Ativos (Protheus)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385289
version: 3
---

---

Através de uma mensagem o TOP envia os dados coletados nos apontamentos de equipamentos para o Manutenção de Ativos (Protheus). Essa mensagem é gerada após o TOP receber os apontamentos provenientes do coletor de forma automática (devido à fórmula visual que foi incluída na tela de apontamentos de equipamentos). Porém caso ocorra alguma inconsistência durante a geração da mensagem o processo deverá ser executado de forma manual.  
Após a execução do processo os apontamentos passam a ter o status definido como "Enviado". Quando ocorrer um erro os apontamentos terão o status igual a "Pendente" e serão sobre esses apontamentos que será realizado o processo manual de Enviar Apontamentos para o Manutenção de Ativos.  
A rotina irá gerar uma mensagem que conterá as informações dos apontamentos de equipamentos e o Manutenção de Ativos receberá e registrará essa mensagem.   
Os códigos dos Centros de Custos devem ser iguais no TOP e Protheus para que os apontamentos sejam corretamente recebidos no Manutenção de Ativos.  
Ao receber os apontamentos de equipamentos será validado se este está associado ao projeto (verificando a informação da filial, que será atualizada no cadastro de equipamentos do RM através do sincronismo do cadastro. A codificação de filiais não utiliza os mesmos códigos nos dois sistemas, por isso o sincronismo dos cadastros deverá tratar a correspondência dos códigos de filiais no TOP e Protheus). Caso não esteja tratada, será gerado log de erro. Antes de efetuar a geração da mensagem para o Protheus, o erro deverá ser corrigido pelo usuário através da correta associação do equipamento à filial.   
Para garantir que a apropriação não seja executada sem a devida correção do cadastro, neste ponto será feita novamente a validação da associação do equipamento à filial do projeto, considerando-se a data do apontamento. Caso não tenha sido corrigido, o registro correspondente não será enviado na mensagem e continuará com o status "Pendente". Esta validação somente ocorrerá se estiver marcado o parâmetro "Valida filial do equipamento" na tela de Parâmetros gerais do TOP.  
Uma vez a mensagem gerada com sucesso então os registros que originaram a mensagem serão atualizados com o status "Enviado".  
Caso ocorram erros no momento da geração da mensagem então os registros permanecerão com o status "Pendente" e poderá ser gerada uma nova mensagem com tais registros acessando novamente a interface e selecionando os registros pendentes.

**Passos para Enviar Apontamentos para o Manutenção de Ativos:**

1. Acessar o TOP;
2. Selecionar o projeto;
3. Acessar o menu Cadastros|Mobilidade|Equipamentos|Apontamentos de Equipamentos;
4. Selecionar os apontamentos que constarão na mensagem;
5. Acessar o menu Processos;
6. Enviar Apontamentos para o Manutenção de Ativos.
