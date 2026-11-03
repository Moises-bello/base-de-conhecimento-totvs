---
article_id: 360061696674
category: Gestão de Frotas
content_hash: 4efd58f97892bbc337fcc5d04645961bad72b08313ae81f7813dbe6994fb4d65
fetched_at: '2026-06-28T22:42:39.382264+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Envio de Pneus para análise técnica ao
  inativar o bem pai
type: support-article
updated_at: '2021-08-13T19:33:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061696674-Manufatura-Linha-Protheus-MNT-Envio-de-Pneus-para-an%C3%A1lise-t%C3%A9cnica-ao-inativar-o-bem-pai
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Ao inativar um bem pai de estrutura é possível enviar os pneus diretamente para **Análise Técnica - MNTA600**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Ao inativar um bem pai de estrutura, é possível alterar o **Status** enviando o pneu para **Análise Técnica**, a partir do passo-a-passo descrito abaixo:

1. Acessar o módulo de **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**.
2. Em **Atualizações / Controle de Pneus / Estrutura / Esquema Mod. 2 -** **MNTA221**, incluir uma estrutura com 4 pneus informando no esquema o mesmo nome da **Família** e **Tipo modelo** do **veículo**, em seguida selecionar o **pneu** e informar a mesma família dos pneus cadastrados e **confirmar**;
3. Incluir uma estrutura com **2 Pneus - engate**, informando no esquema o mesmo nome da **Família** e **Tipo modelo** do **bem**, em seguida selecionar o pneu e informar a mesma família dos pneus cadastrados e **confirmar**.
4. Em **Atualizações / Controle de Oficina / Ordem de serviço / Corretiva / Corretiva - MNTA420**, incluir uma **Ordem de Serviço - O.S** corretiva de movimentação de pneu para o**Bem - engate** e **Veículo** incluindo anteriormente;
5. Abrir a **O.S.** em **Rodados**, incluir os pneus para cada localização gerada no **Esquema Mod. 2 - MNTA221**.
6. Fazer esse procedimento para as duas **O.S**.
7. Em **Atualizações / Controle de Oficina / Bens / Estrutura de Bens - MNTA090** selecionar a **Estrutura do Veículo** e **Alterar**. Incluir na estrutura os**bens  - engate e motor**. Deverá carregar a baixo do engate o pneus que foram incluídos em sua estrutura.
8. Em **Atualizações / Controle de Oficina / Bens / Veículo - MNTA084** selecionar o **Veículo**que possui a estrutura e em **Ações Relacionadas** selecionar **Inativar**;
9. Abrirá uma tela para inativação do bem e sua estrutura. Informar os campos obrigatórios para inativação;
10. Verificar que ao selecionar um dos pneus e clicar em **Status,** será aberta uma nova tela, com todos os campos necessários para enviar os **Pneus** para análise. Informar um novo **Status** e verificar que conforme o **Status** informado, será liberado ou não os campos para edição;
11. Informar dados aos pneus de forma que alguns sejam enviados para análise e outros inativados - Verificar botão de legenda para saber os destinos;
12. Confirmar a inativação do **veículo** e verificar que os pneus que foram selecionados para serem enviados para analise continuam como ativos no **Cadastro de pneus**. Inclusive esses mesmo pneus devem estar disponível para utilização em outras estruturas imediatamente.
13. Em **Atualizações / Controle de Pneus / Análise Técnica / Análise Técnica - MNTA600** verificar que foi gerado registro para os pneus marcado para serem enviados para **Análise Técnica**.

**Saiba mais**  
Para habilitar o botão **Rodados**, verifique o conteúdo do artigo [Configuração botão Rodados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028080352)
