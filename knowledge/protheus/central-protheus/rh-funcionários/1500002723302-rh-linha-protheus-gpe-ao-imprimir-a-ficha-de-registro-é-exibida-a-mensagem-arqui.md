---
article_id: 1500002723302
category: RH - Funcionários
content_hash: 28f4dfde3987d16ed700c34e5a325789f6ffcfdfd6bd05e755a2c47fba5c2d3f
fetched_at: '2026-06-28T22:43:27.368351+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Ao imprimir a Ficha de Registro, é exibida a mensagem
  ARQUIVO/system/arquivo.bmp já existe. Regrava
type: support-article
updated_at: '2025-04-25T19:56:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002723302-RH-Linha-Protheus-GPE-Ao-imprimir-a-Ficha-de-Registro-%C3%A9-exibida-a-mensagem-ARQUIVO-system-arquivo-bmp-j%C3%A1-existe-Regrava
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31669742743319)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Ao imprimir a **Ficha de Registro - GPEA260**, é exibida a mensagem ARQUIVO/system/arquivo.bmp já existe. Regrava?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Esta mensagem é apresentada para funcionários que possuem transferência entre filiais e utilizam o arquivo de foto com a mesma nomenclatura, desta forma quando é solicitado para imprimir o sistema exibe o alerta informando que a imagem já existe. A rotina questiona se você deseja sobrepor o arquivo, optando por não a ficha é impressa sem foto. Utilizando o **Configurador**, através da rotina **Repositório de Imagens**, deve ser efetuada a carga de uma imagem com a nomenclatura diferente, pode ser utilizada a mesma foto, precisa apenas ter um nome diferente para o arquivo.  
  
Para efetuar a importação, siga os passos abaixo:  
  
 1. Acesse o **Configurador** -> **Ambiente** -> **Cadastros** -> **Repositório de Imagens** 2. Clique em **Incluir** 3. Selecione a pasta onde se encontra as imagens, e clique **Abrir** 4. ***Flag*** a imagem a ser importada, e clique **Confirmar** 5. Depois de importado, clique em **OK** 6. Acesse o módulo **SIGAGPE - Gestão de Pessoal** 7. Acesse **Atualizações** -> **Funcionários** -> **Funcionários** 8. Selecione o funcionário e clique em **Alterar** 9. Na aba **Cadastrais**, clique em **Opções de Imagem** e posteriormente em **Imagem**10. Selecione foto do funcionário salva no **Repositório de Imagens** e clique em **Ok**11. ***Flag*** a opção **Ajustar** e clique em **Salvar.****Saiba Mais**

[RH - Linha Protheus - GPE - O que é a Ficha de Registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053273114-RH-Linha-Protheus-GPE-O-que-%C3%A9-a-Ficha-de-Registro?source=search)

[RH - Linha Protheus - GPE - Não imprime ficha de Registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403219483927-RH-Linha-Protheus-GPE-N%C3%A3o-imprime-ficha-de-Registro?source=search)

[RH - Linha Protheus - GPE - Como imprimir uma ficha de registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11565647253911-RH-Linha-Protheus-GPE-Como-imprimir-uma-ficha-de-registro?source=search)

[RH - Linha Protheus - GPE - Como Incluir Foto no Cadastro do Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007135072-RH-Linha-Protheus-GPE-Como-Incluir-Foto-no-Cadastro-do-Funcion%C3%A1rio?source=search)
