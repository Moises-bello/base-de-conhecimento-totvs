---
content_hash: 1f98dc30f7d123efd3b61320471d6ed1948c901cfd5f5b00b00f08304b1c9d48
fetched_at: '2026-06-29T00:08:38.974598+00:00'
page_id: '286003966'
product: rm
source: tdn-rm
title: Como fazer CAGED Novos campos para o Exame Toxicológico Registro C
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286003966
version: 115
---

# CAGED

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Emissão dos novos campos para o Exame Toxicológico no Registo C. |
| **Situação/Requisito:** | Contemplar os novos campos para o Exame Toxicológico no Registo C. |
| **Solução/Implementação:** | A legislação do CAGED que entra em vigor a partir de 16 de agosto de 2017, referente a Portaria nº 116/2016 obriga o empregador que admitir ou desligar motoristas  profissionais a declarar os campos: Código Exame Toxicológico, Data  Exame Médico (Dia/Mês/Ano), CNPJ do Laboratório, UFCRM e NRCRM,  relativos às informações do exame toxicológico de que trata o art. 24 da  Lei nº 7.998, de 11 de janeiro 1990, os quais foram incluídos no layout  do registro C     Os funcionários que terão os novos campos acrescidos nos registros “C” ou “X” serão:      1. Os admitidos ou demitidos no Mês e; 2. Código do CBO PFUNCAO.CBO2002 igual a um dos códigos abaixo (somente números):          2.1.     782310 - Motorista de furgão ou veículo similar;            2.2.     782320 - Condutor de ambulância;            2.3.     782405 - Motorista de ônibus rodoviário;            2.4.     782410 - Motorista de ônibus urbano;            2.5.     782415 - Motorista de trólebus;            2.6.     782505 – Caminhoneiro autônomo (Rotas regionais e internacionais);            2.7.     782510 - Motorista de caminhão (Rotas regionais e internacionais); e            2.8.     782515 – Motorista operacional de guincho.      3.    Observação: Caso a competência do CAGED não seja a Atual, deve verificar o Histórico de função para obter o CBO       Nos registros C e X, para os funcionários que satisfaçam as condições acima, após o campo “CEP Residência do Trabalhador” deverá informar:     Código Exame Médico, Data Exame Médico (DDMMAAAA), CNPJ LABORATÓRIO, UF DO MÉDICO e CRM DO MÉDICO.     Porém para os funcionários que não possuem os CBO´s acima os campos devem ficar em branco com 51 espaços. Totalizando um filler de 81 espaços.    **PROCEDIMENTO PARA IMPLANTAÇÃO.**  Instalar os últimos patch do Release a partir da versão 12.1.15. Rodar o script fechado criado pelo SSO , acesse o link **<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ExecutorScriptCaged.aspx>** para saber como fazer. Importar o layout **TOTVS Report “FOPREL0014 - Caged para conferência.TotvsReport** que contempla os novos campos    **PROCEDIMENTO PARA CONFIGURAÇÃO**  Integrar o LABORE com o Vitae      Cadastre o exame que será usado para determinar o Exame toxicológico.         Parametrize o SSO informando o novo exame toxicológico cadastro para ser usado para compor os novos campos do registro C do CAGED.            Cadastre o Médico para obtenção do CRM e seu UF      Cadastre a Entidade (Laboratório) responsável pela realização do Exame Toxicológico para obtenção do CNPJ      Relacione no Convênio a Entidade Laboratório com o Exame Toxicológico          Na Folha de Pagamento no Anexo Segurança e Medicina da Visão de funcionário cadastre a consulta e o exame toxicológico admissional ou Demissional        Inclua a Consulta Médica relacionada ao Exame Toxicológico          Após salvar a consulta médica inclua o Exame Toxicológico      Informe os dados do Exame. O campo Tipo de exame é fundamental para que o CAGED saiba se o exame é admissional ou demissional.        Após Cadastrar no prontuário o Exame Toxicológico para Admissão ou Demissão. Pode-se emitir o CAGED em RH \ Folha de Pagamento \ Encargo \ CAGED.        Os novos campos são contemplados nas seguintes saídas:   Conferência em Tela:         Conferencia no layout para arquivo texto         Arquivo a ser importado pelo Validador do CAGED.        Caso o CBO da função seja o de motorista (um dos listados acima), as seguintes situações poderão gerar mensagens de aviso no log:   * Esquecer de informar o código do exame no parametrizador; * Esquecer de preencher algum campo exigido; * Cadsatrar o exame posterior à admissão ou mais de 120 dias após demissão; * Informar o tipo do exame (admissional/demissional) erroneamente ou esquecer de informar; * Agendar exame diferente do que consta no parametrizador.        Para mais informação sobre a consulta médica acesse: <http://wikihelp.totvs.com.br/WikiHelp/SMT/SMT.ProntuarioMedico.aspx> |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
