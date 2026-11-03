---
content_hash: aac45fc013dc609df1d1a8c0192060f45b9d1a036db4a936c5beb93f4b1e3913
fetched_at: '2026-06-29T00:11:39.962267+00:00'
page_id: '791847949'
product: rm
source: tdn-rm
title: Previdência Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=791847949
version: 15
---

false

**A partir das Versões:**

* 12.1.2302.231
* 12.1.2306.177
* 12.1.2310.112 e Superiores.

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**
4. **Informações complementares**

## **01. VISÃO GERAL**

Nesta tela, você poderá estabelecer a conexão entre as Entidades de Previdência Complementar e os eventos relacionados à previdência complementar que são inseridos no envelope de pagamento.

## **02. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

1) Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, acesse Menus e permita o acesso ao cadastro **09.01.15 - Previdência Complementar**

2) Acesse o menu Administração de Pessoal | Eventos | Eventos, verifique as configurações dos eventos de Previdência Complementar. Na aba "Incidências", tanto em "Descontos" quanto em "Proventos", é possível vincular o Tipo de Previdência Complementar, caso o evento não utilize nenhum código de cálculo.

Para que o grupo "previdCompl" seja incluído no evento S-1210, é necessário configurar os eventos de acordo com os códigos "codIncIRRF" (46, 47, 48, 61, 62, 63, 64, 65, 66). Para o tipo de previdência - Privada, os códigos a serem utilizados são "codIncIRRF" (46, 47, 48). No caso do tipo de previdência - Fundação de Aposentadoria Programada Individual - FAPI, devem ser aplicados os códigos "codIncIRRF" (61, 62, 66). Para o tipo de previdência - Fundação de previdência complementar do servidor público - Funpresp, os códigos apropriados são "codIncIRRF" (63, 64, 65). Se houver uma associação entre o tipo de previdência e um código "codIncIRRF" que não corresponda ao correto, irá ocorrer um erro na geração do arquivo xml S-1210. É importante observar que os registros feitos neste menu não são salvos na DIRF.IMPORTANTE!

true2Cadastro Previdência ComplementarCadastro Previdência Complementar

Acesse o menu eSocial | Previdência Complementar | Cadastro Previdência Complementar

Crie conforme tipo de previdência desejado:

Após salvar, vá para a aba de **Eventos da previdência complementar** e associe os eventos que foram configurados de acordo com o item 2 na aba de parametrização. Para os eventos de décimo terceiro foi disponibilizado o campo "**Décimo Terceiro**" para a impressão da tag vlrDedPC13 a partir do leiaute 1.3.

Para que o grupo "previdCompl" seja incluído no evento S-1210, é necessário configurar os eventos de acordo com os códigos "codIncIRRF" (46, 47, 48, 61, 62, 63, 64, 65, 66). Para o tipo de previdência - Privada, os códigos a serem utilizados são "codIncIRRF" (46, 47, 48). No caso do tipo de previdência - Fundação de Aposentadoria Programada Individual - FAPI, devem ser aplicados os códigos "codIncIRRF" (61, 62, 66). Para o tipo de previdência - Fundação de previdência complementar do servidor público - Funpresp, os códigos apropriados são "codIncIRRF" (63, 64, 65). Se houver uma associação entre o tipo de previdência e um código "codIncIRRF" que não corresponda ao correto, irá ocorrer um erro na geração do arquivo xml S-1210. É importante observar que os registros feitos neste menu não são salvos na DIRF.IMPORTANTE!

true3Conversor Perfil DIRF x Previdência ComplementarConversor Perfil DIRF x Previdência Complementar

Esse processo tem como objetivo buscar os dados informados na aba "Previdência Complementar" dos perfis da DIRF e gravá-los no Cadastro de "Previdência Complementar" do eSocial, especialmente para os dados que estão exclusivamente nos perfis da DIRF.

1) Acesse o menu eSocial | Previdência Complementar | Conversor Perfil DIRF x Previdência Complementar, para que seja apresentada a tela de geração do processo:

2) Clique em avançar:

3) Informe a coligada desejada e clique em avançar:

4) Clique em executar:

**Observações:**

* É imprescindível salvar um perfil no processo **DIRF/Informe de Rendimentos** com os dados da Previdência complementar; caso contrário, o processo não copiará os dados.
* A criação dos cadastros ocorrerá somente para aqueles que possuírem eventos vinculados na DIRF, seja Privada, Fundo de Aposentadoria Programa Individual (FAPI) ou Fundação de Previdência Complementar do Servidor Público (Funpresp).
* Se um registro do cadastro de "Previdência Complementar" for excluído e a origem for do conversor, ele será reinseridos quando o processo for executado novamente, com o mesmo código de eventos.
* Ao cadastrar uma Previdência Complementar pelo Parametrizador da DIRF, a partir da versão desse documento, ela será automaticamente incluída no cadastro de "Previdência Complementar" do eSocial.

## **03. TABELAS UTILIZADAS**

PPREVIDENCIACOMPLEMENTAR, PPREVIDENCIACOMPLEMENTAREVENTO.

## **04. Informações complementares**
