---
content_hash: 8bb9899dc66e801984c32fecfe54b928674c4e8a10c1274511d4963775693c8a
fetched_at: '2026-06-29T00:10:31.681020+00:00'
page_id: '521648158'
product: rm
source: tdn-rm
title: RMFIS00001_REINF R-1000 – Informações do Contribuinte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521648158
version: 21
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.27 |
| **Ocorrência:** | Evento R-1000 – Informações do Contribuinte |
| **Ambiente:** |  |
| **Passo a passo:** | Evento em que são fornecidas pelo contribuinte informações cadastrais necessárias ao preenchimento e validação dos demais eventos da EFD-Reinf, inclusive para apuração das retenções e contribuições devidas. Este é o primeiro evento que deve ser transmitido pelo contribuinte. As informações para geração deste evento serão provenientes do Cadastro de Filiais e do Anexo Dados Fiscais.  Uma vez enviado com sucesso o registro não será mais enviado. A não ser quando algum campo que é controlado pelo [Log de Alterações](https://tdn.totvs.com/display/LRM/Log+de+Filial) for alterado.   121º Passo1º Passo**Pré-requisito** Enviar o Evento R-1000 no TAF com a data final preenchida:  Execute o aplicativo TAF e realize a apuração e transmissão do evento R-1000 com a data final preenchida no complemento cadastral conforme imagem:   Imagem      ATENÇÃO   Ao preencher o campo Dt Fim Per, certifique-se que todos os eventos periódicos do mês foram transmitidos e o período esteja encerrado.  Exemplo:  Dt Fim Per = 12/2019  Eventos periódicos do mês 12 transmitidos e autorizados, inclusive com o Fechamento dos Eventos Periódicos (R-2099) também autorizado.       32º Passo2º Passo Acesse o RM e realize as conferências abaixo:  Certificado importado conforme documentação: [Importação de Certificado](https://tdn.totvs.com/pages/viewpage.action?pageId=521652215)  Parâmetros preenchidos conforme documentação: [Parâmetros de Integração (TSS)](https://tdn.totvs.com/pages/viewpage.action?pageId=521648108)  Após conferência acesse o menu Obrigações Acessórias | SPED | EFD-Reinf | Eventos Cadastrais.   Imagem  43º Passo3º Passo Realize a inclusão do registro, tipo: "Evento R-1000".  O campo "Data Inicial" deve ser preenchido com a data de início do período da validade das informações prestadas no evento  O campo "Data Final" não possui preenchimento obrigatório.   Imagem  54º Passo4º Passo Selecione o evento | Menu Processos | Transmitir Evento   Imagem  65º Passo5º Passo Após a transmissão do evento o status é alterado para "Pendente". É necessário executar o processo "Consultar Evento", conforme imagem, para visualizar o retorno da Receita Federal.   Imagem  76º Passo6º Passo Após realizar a consulta o evento é autorizado.  Em "Anexos | Histórico do Evento" é possível visualizar todo o histórico de ocorrências conforme exemplo na imagem abaixo:   Imagem |
| **Observações:** |  |
