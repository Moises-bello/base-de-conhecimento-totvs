---
content_hash: 6ad4b980f8799140e6da80050112afc0a04bf110adc03f3a9f4754d1206a529c
fetched_at: '2026-06-29T00:09:30.916580+00:00'
page_id: '425458561'
product: rm
source: tdn-rm
title: RM Portal - Parâmetros Gerais 1/18
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458561
version: 13
---

---

**Dados do Aluno**

**Consulta das turmas do professor**

**Exibir telefone do aluno:** ao marcar este parâmetro, será exibido os dados referente ao telefone do aluno quando o professor clicar na opção: Portal | Diário de Classe | Alunos.

**Exibir e-mail do aluno**: ao marcar este parâmetro, será exibido o e-mail do aluno quando o professor clicar na opção: Portal | Diário de Classe | Alunos.

**Exibir data de nascimento do aluno**: ao marcar este parâmetro, será exibido a coluna de data de nascimento do aluno quando o professor clicar na opção: Portal | Diário de Classe | Alunos.

**Alteração de dados cadastrais/profissionais do aluno**

A alteração dos dados cadastrais /profissionais do aluno, permitirá que o aluno/responsável visualize e/ou altere os dados cadastrais conforme a marcação dos parâmetros abaixo.  
**Apenas consulta:** o aluno/ responsável poderá apenas visualizar os dados.  
**Solicitar alteração para filial do aluno:** permitirá que os alunos altere os dados, porém, a alteração não ficará disponível. Após salvar, o portal irá apresentar uma mensagem informando que a solicitação foi encaminhada com sucesso, e será enviado um e-mail para a filial para que a IE possa alterar os dados informando pelo aluno.  
**Solicitar alteração para o Nível de Ensino do aluno:** permitirá que os alunos altere os dados, porém, a alteração não ficará disponível. Após salvar, o portal irá apresentar uma mensagem informando que a solicitação foi encaminhada com sucesso, e será enviado um e-mail para a o Nível de Ensino em que o aluno está matriculado e a IE irá alterar os dados informando pelo aluno.  
**Permitir alteração (Atualização será feita diretamente na base de dados):** permitirá que o aluno altere os dados e a informação será gravada diretamente na base de dados.

**Alteração de foto do perfil do aluno**

**Permitir alterar a foto (formatos permitidos: JPEG, JPG, tamanho máximo: 3MB):** responsável por permitir o aluno alterar a foto, seja incluir uma nova, alterar ou excluir uma existente.

**Usar Inteligência Artificial para validação das** **imagens**: responsável por habilitar o recurso de validação de fotos por inteligência artificial. Entretanto é importante informar que, neste momento, essa funcionalidade está em modo **trial** e não possui custos adicionais para sua utilização. No entanto, ressaltamos que, futuramente, este serviço poderá ser tarifado. Caso a funcionalidade passe a ser cobrada, garantimos que todos os clientes serão previamente avisados com antecedência, permitindo que avaliem a continuidade de seu uso conforme suas necessidades. O objetivo deste parâmetro é validar se de fato a foto que o usuário está informando é realmente válida, sendo que está validação estará sendo feito via inteligência artificial. Ao habilitá-lo duas mensagens serão exibidas ao usuário, sendo a primeira referente a versão **trial**.

E a segunda é referente a obtenção do consentimento da pessoa antes de utilizar a foto em um processo que envolva inteligência artificial (IA). Na mensagem possui um exemplo de uma cláusula no contrato acadêmico/financeiro do aluno ou no termo de consentimento de uso de imagem e voz.

**Usar cláusula de validação**: parâmetro **obrigatório** que deve indicar onde esta cláusula irá estar seja no contrato acadêmico/financeiro do aluno ou no termo de consentimento de uso de imagem e voz. Vale frisar que ao escolher **contrato** nenhuma validação irá ocorrer, ele apenas é de caráter informativo, por outro lado se escolher **termo de consentimento de imagem e voz** o usuário somente poderá fazer o upload ou exclusão de fotos se tiver dado o aceite no termo, caso contrário não irá conseguir prosseguir. Outro ponto bem importante que este campo não irá ter nenhuma interferência em nenhum relatório criado.

**Regra de validação das imagens****:** campo obrigatório, ele que irá conter a regra explícita de validação da IA. Existe uma regra padrão que já vem configurada, sendo possível editar ou restaurar a padrão (clicando no botão **Restaurar textos**).

**Mensagem padrão de orientação para upload de** **foto**: campo de mensagem padrão de orientação para o upload de foto, este texto informado tem o objetivo de ser exibido no modal que seleciona a foto a ser enviada. Um texto padrão já vem configurado, sendo possível editar ou restaurar (clicando no botão **Restaurar textos**). Caso este campo estiver vazio, nenhum texto será exibido no modal mencionado.

Texto de orientação sendo exibido no portal.

Vale ressaltar que ao clicar no botão **Restaurar textos** ele restaura o padrão da **Regra de validação das imagens**e do campo **Mensagem padrão de orientação para upload de foto.**Comportamento depreciado

Até a versão 12.1.2502.102 a tela da parametrização está da forma abaixo
