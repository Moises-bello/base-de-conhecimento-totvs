---
content_hash: a0300ff812c1931b53e28e26d8afff54b203215d0a240990a7dc78d4dadf5065
fetched_at: '2026-06-29T00:08:54.853406+00:00'
page_id: '346500860'
product: rm
source: tdn-rm
title: RMFIS00001_REINF R-1000 – Informações do Contribuinte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346500860
version: 20
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal x TAF Totvs Automação Fiscal |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Evento R-1000 – Informações do Contribuinte |
| **Ambiente:** |  |
| **Passo a passo:** | Evento em que são fornecidas pelo contribuinte informações cadastrais necessárias ao preenchimento e validação dos demais eventos da EFD-Reinf, inclusive para apuração das retenções e contribuições devidas. Este é o primeiro evento que deve ser transmitido pelo contribuinte. As informações para geração deste evento serão provenientes do Cadastro de Filiais e do Anexo Dados Fiscais.  Estas informações são enviadas para o TAF através do Registro T001 do Layout TAF. Uma vez enviado com sucesso o registro não será mais enviado. A não ser quando algum campo que é controlado pelo [Log de Alterações](http://tdn.totvs.com/display/LRM/FISCAL01-909+DT+Log+do+Cadastro+da+Filial) for alterado. Neste caso, o registro deve ser reenvido para o TAF para posterior envio ao Fisco.   121º Passo1º Passo**Pré-requisito** Cadastro de Filial criado no TAF.  Existem duas maneiras de criar uma estrutura de empresas no TAF:  1. Conceito Empresa / Filial 2. Conceito de Gestão de Empresas  Mais detalhes do cadastro de Filial e estrutura da empresa acesse: [Cadastro da Empresa - TAF - P12](http://tdn.totvs.com/display/TAF/Cadastro+da+Empresa+-+TAF+-+P12)    Após o cadastro de empresa execute o aplicativo através do ícone TAF\_Client     32º Passo2º Passo Informe o usuário “admin”, deixe o campo referente a senha vazio ou informe a senha caso possua e clique no botão “Entrar”:     43º Passo3º Passo Acesse o menu Atualizações | Empresa | Complemento Cadastral   54º Passo4º Passo Altere o complemento cadastral TAF e preencha os campos Filial TAF e Cod Filial, onde o Cod Filial será utilizado na integração com sistemas externos  Observação:  O campo "Cod Filial" deve ser preenchido com o mesmo valor do campo "Código da Filial em sistemas externos" informado no cadastro da filial da linha RM, aba "Dados Adicionais" conforme imagens abaixo:     65º Passo5º Passo O usuário pode preencher apenas os demais campos obrigatórios, pois esse cadastro será atualizado no momento da integração RM X TAF.  Após salvar o cadastro acessar o documento:  para realizar a integração RM X TAF. 76º Passo6º Passo Após realizar a integração RM X TAF acessar o menu Atalizações | Eventos Reinf | Apuração     87º Passo7º Passo Conferir a data da apuração, marcar a opção R-1000 Informações do Contribuinte e utilizar a função "Processar" conforme a imagem abaixo:   98º Passo8º Passo Após seguir os passos anteriores o registro terá o status atualizado conforme a legenda:    Para visualizar a apuração acesse o botão "Visualizar Apurações"       109º Passo9º Passo Para que o registro seja transmitido ao governo utilize o botão Monitor conforme imagem abaixo:    Será apresentado o Monitor de Transmissão do REINF, onde pode ser selecionado o evento a ser transmitido, entre Tabelas, eventos Periódicos e Não Periódicos.   1110º Passo10º Passo Para realizar a transmissão selecione o registro e clique no botão Transmitir conforme destacado na imagem:      Na opção Monitorar Transmissões é possível visualizar a mensagem de retorno da Transmissão. Caso exista alguma inconsistências é necessário ajustar e transmitir novamente. |
| **Observações:** | Mais informações através do documento:  Video do Processo:  [HOW TO - TAF - Apurações para geração de XML´s REINF - R1000 e R1070](https://youtu.be/7LWKImXXMQw) |
