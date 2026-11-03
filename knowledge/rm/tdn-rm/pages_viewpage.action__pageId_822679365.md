---
content_hash: 9b79e7d78a84e14ccdd26506cbe9582cca32d46e6eccda55ed1bffd4a223df91
fetched_at: '2026-06-29T00:11:46.060883+00:00'
page_id: '822679365'
product: rm
source: tdn-rm
title: Grupo de informações relativas ao prestador do serviço - NFS-e Nacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822679365
version: 14
---

Acentuação e Caracteres especiais

Este grupo tem campos sujeitos a tratamento automático para remover acentuação e caracteres especiais. Para mais informações consulte a documentação especifica.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **prest** | **DPS/infDPS/** | **Sim** | **Origem** | **Grupo de informações relativas ao prestador do serviço.** |
| CNPJ | DPS/infDPS/prest/ | Sim | Conforme o cadastro da filial do movimento. | Tag que leva o CNPJ do prestador do serviço cadastrado na Filial do RM. |
| CAEPF | DPS/infDPS/prest/ | Não | Cadastro da Filial | Dados Adicionais| Inscrição Municipal l Campo "Cadastro de atividade econômica de pessoa física".  GFILIAL.CADATIVECONOMECAPF | Cadastro de Atividade Econômica de Pessoa Física caso não possua CNPJ. |
| IM | DPS/infDPS/prest/ | Sim | Cadastro da Filial | Dados Adicionais| Inscrição Municipal  GFILIAL.INSCMUN | Inscrição Municipal do prestador do serviço cadastrada na Filial do RM.  Este campo só será gerado se o parâmetro "Possui Cadastro Nacional de Contribuinte" estiver marcado nos dados fiscais da filial. Imagem   Para manter a máscara da inscrição municipal é necessário marcar a opção de "Não Remover Máscara IM Prestador" nos [dados fiscais do município.](https://tdn.totvs.com/pages/viewpage.action?pageId=652399054) |
| xNome | DPS/infDPS/prest/ | Sim | Cadastro da Filial | Identificação | Nome Fantasia  GFILIAL.NOMEFANTASIA | Nome da Filial localizado no cadastro da Filial do RM. |
| end | DPS/infDPS/prest/ | Não |  |  |
| Fone | DPS/infDPS/prest/ |  | Cadastro da Filial | Endereço | Telefone  GFILIAL.TELEFONE | Localizado na aba Endereço do cadastro da Filial. |
| email | DPS/infDPS/prest/ |  | Cadastro da Filial | Endereço | email  GFILIAL.EMAIL | Localizado na aba Endereço do cadastro da Filial. |
