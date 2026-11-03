---
content_hash: 4d2b904d84050a120b09d04ab2d20d0ce53f98d0f53e57b0bfbb8fc6bcbf63a3
fetched_at: '2026-06-29T00:10:35.625725+00:00'
page_id: '531023336'
product: rm
source: tdn-rm
title: Controle de Ocupação de Leitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531023336
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas utilizadas**
4. **Regras e Validações**

sumarioVisão Geral

## **01. VISÃO GERAL**

No menu "Controle de Ocupação de Leitos", permitir alterar o status do leito para Isolado e também cancelar o isolamento do leito. Deverá ser configurado controle de acesso tanto para isolar quanto para cancelar (No cadastro de Perfis). No momento do isolamento/cancelamento deverá ser logado as alterações: responsável pela alteração, data hora, ação realizada (isolou, cancelou, ocupou), motivo do isolamento.  
No menu "Controle de Ocupação de Leitos", será possível fazer reserva de leito e cancelamento da reserva de leito, caso o usuário tenha permissão de acesso. No momento da reserva/cancelamento deverá ser logado as alterações: responsável pela alteração, data hora, ação realizada (reservou, cancelou, ocupou), motivo da reserva/cancelamento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para alterar o status do leito, basta seguir o passo a passo abaixo: 

Telas Utilizadas

## **03. TELAS UTILIZADAS**

No TOTVS Gestão Hospitalar acesse o menu**Atendimento> Internação> Controle de Ocupação de Leitos.**

2.Na tela de Controle de Ocupação de Leitos teremos todos os leitos identificados pelas cores que representam o estado atual de cada um.

3. Para alterar o status do leito selecione-o e clique em **Controle** e clique na ação de deseja realizar.

4. Em todo caso você terá que descrever um **Motivo** e selecionar a **Ação** desejada e clique em **Salvar/OK.**

5. Para o Cancelamento de Ação também é necessário que descreva **Motivo**.

A partir da versão 12.1.2510 o status Aguardando Supervisão, do Kanban de , passa a aparecer na tela de controle de leitos:

 Regras e Validações

## **04. Regras e Validações**

04.01 Fluxo

O fluxo padrão de atendimento seguirá a seguinte ordem de status do leito:  
1- Livre;  
2- Ocupado (Quando algum paciente for alocado ao leito);  
3- Aguardando Higienização (Quando houver alta do paciente e o mesmo liberar o leito);  
4- Em Higienização;  
5- Livre;

Os status de "Em Serviço/Manutenção", "Isolado" e "Reservado" serão apenas utilizados via os processos do menu de "Controle" da tela.

04.02 Isolamento de Quarto de Leito

**Obs.: Este processo só funcionará caso o leito estiver vinculado a um quarto:**

**Ao tentar realizar o Isolamento de um Quarto de Leitos, o processo vai seguir as seguintes premissas:**

1- Se ambos leitos estiverem com o status "Livre" ou apenas 1 dos Leitos do Quarto estiver "Ocupado", o status de todos os Leitos serão alterados para "Isolado";  
2- Caso exista mais de 1 paciente nos Leitos do Quarto, ao tentar realizar o isolamento, será exibida a seguinte mensagem:

**Para o Cancelamento do Isolamento do Quarto, o processo irá seguir as seguintes premissas:**

1- Se existir nenhum ou apenas 1 paciente no quarto, todos Leitos associado ao Quarto serão alterados para o status "Aguardando Higienização";  
2- Caso exista múltiplos Pacientes no mesmo Quarto, o Isolamento será desfeito e o status do Leito permanecerão "Ocupado" devido o fato do paciente ainda estar hospedado no mesmo.

Obs.: Ao realizar a alta de um paciente que esteja em um Quarto, caso ele fosse o único paciente do mesmo e o Quarto estiver em Isolamento, o status de todos os Leitos do Quarto serão alterados para "Aguardando Higienização". Caso o Quarto não esteja Isolado, apenas o status do Leito "Ocupado" será alterado.

Obs.²: Ao realizar a alta de um paciente que esteja em um Quarto esteja "Isolado" e existam outros pacientes, o status de "Isolado" se manterá até que o último paciente receba alta.
