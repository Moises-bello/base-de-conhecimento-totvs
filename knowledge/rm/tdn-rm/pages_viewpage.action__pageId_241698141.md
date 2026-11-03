---
content_hash: 8c704d1a1ca20be3deed781ce870e8319ec13eea917d2654a54825896ee02094
fetched_at: '2026-06-29T00:08:10.869846+00:00'
page_id: '241698141'
product: rm
source: tdn-rm
title: TULEC0_DT_Considera_Extras_Refeição_Dentro_Do_Intervalo_De_Ausência_Planejada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=241698141
version: 110
---

# Parâmetros Coletivos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Automação de Ponto* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parâmetros do sindicato.* | *Parâmetros do sindicato.* | |
| **Cadastros Iniciais:** | *Deverá cadastrar horários que possuam ausência planejada ou limite de refeição de acordo com o tipo de horário.* |
| **Parâmetro(s):** | *No parametrizador do sindicato associado ao funcionário deverá avançar até a etapa EXTRA e marcar a opção "Considera extras de refeição dentro do intervalo de ausência planejada".* |
| **Chamados Relacionados** | *TULEC0* |
| **País(es):** | *Todos países.* |
| **Banco(s) de Dados:** | *Oracle e SQL.* |
| **Tabelas Utilizadas:** | *APARCOL* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Implementado parâmetro no sindicato na Etapa Extra "Considera extras de refeição dentro do intervalo de ausência planejada". Marcando este parâmetro as extras realizadas durante o intervalo de ausência planejada serão calculadas como extras de refeição, caso esteja desmarcado o sistema calculará extras normais conforme já era realizado anteriormente.

## Procedimento para Utilização

       1.            Acessar a MDI selecionando o contexto "TOTVS Automação de Ponto";

       2.            Os funcionários que terão a diferenciação das horas extras de refeição deverão ter no horário vinculado limite de refeição ou ausência planejada cadastrada, isto de acordo com o tipo de horário.

       3.            Acessar o menu Configurações | Eventos, cadastrar um novo evento a ser calculado (este é o evento do TOTVS Automação de Ponto), e associar o código de cálculo 0043 (Tipo Ocorrência), clicar em SALVAR;

       4.            Ainda com a tela de edição do evento criado no passo anterior deverá clicar em Anexos | Evento por tipo de ocorrência e associar a ocorrência ERA (Extra Refeição Autorizado).

       5.            Acessar o menu Configurações | Parametrizador | Sindicato, editar o sindicato que terá a diferenciação das extras referente ao intervalo de ausência planejada;

       6.            Avançar até a Etapa 2 - Extra e marcar a opção "Considera extras de refeição dentro do intervalo de ausência planejada";

       7.            Ainda no parametrizador do sindicato deverá avançar até a Etapa 17 - Eventos e incluir o evento com código de cálculo 0043, cadastrado anteriormente e associar o evento do relacionado do RM Labore que receberá os valores calculados no movimento do funcionário;

       8.            O funcionário deverá ter batidas lançadas no período para o intervalo de ausência de planejada (intervalo de refeição) e estas batidas deverão compreender um número de horas menor  do que o cadastrado para este intervalo, sendo assim calculadas horas extras referente a este intervalo;

        9.           Efetuar o recálculo do espelho do funcionário e conferir na aba do espelho do funcionário, Ocorrências os registros existentes com a ocorrência ERA (Extra de Refeição Autorizada);

        10.         Conferir também na aba Movimento do espelho do funcionário o evento associado do RM Labore com o valor de extras de refeição calculado.

divs
