---
article_id: 19403698359575
category: Administração de Pessoal
content_hash: 7160c1d700830eec9cf6034d942b37bee7adedda4146c05ed2796a29d6ff407a
fetched_at: '2026-06-28T22:47:01.201706+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Parametrização e Cadastro do Histórico Dados Cadastrais Futuro
type: support-article
updated_at: '2025-03-05T17:22:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19403698359575-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-e-Cadastro-do-Hist%C3%B3rico-Dados-Cadastrais-Futuro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19403668479511) Tempo aproximado para leitura: **00:03:10 min****Dúvida**Como parametrizar o sistema para que seja realizada as alterações dos dados cadastrais do funcionário para competências futuras, sem a necessidade de alterar diretamente no cadastro do funcionário?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2310.120
* e Superiores.

**Solução**Para facilitar esse processo, foi disponibilizado o parâmetro "Utiliza controle de Alteração de Dados Cadastrais futuro". Com essa configuração, o sistema passa a armazenar as alterações cadastrais futuras em um novo cadastro.

Para atualizar o cadastro do funcionário com essas alterações, o usuário pode parametrizar a atualização na liberação de competência ou executar o processo "Efetivar Dados Cadastrais".

É importante observar que nenhuma rotina do produto buscará o salário desse novo cadastro, continuando a buscar o salário do cadastro original do funcionário.

1. Para atender essa demanda foi necessário a criação do anexo **"Histórico Dados Cadastrais Futuro "**, e para a liberação desse anexo é necessário a execução do script pelo aplicativo RM.Atualizador.exe.

![](https://tdn.totvs.com/download/attachments/687158765/image2021-9-8_9-20-29.png?version=1&modificationDate=1652970707523&api=v2)

2. Acesse o menu **Configurações | Parametrizador | Funcionário | Restrições Cadastrais** e marque o parâmetro  "**Utiliza Controle de Dados Cadastrais Futuro**".

![](https://tdn.totvs.com/download/attachments/687158765/image-2023-11-13_9-14-55.png?version=1&modificationDate=1699877695593&api=v2&effects=border-simple,shadow-kn)

3. Acesse o módulo **Serviços Globais | Segurança | Perfis**, após isso selecione o sistema **Folha de pagamento** conforme as imagens abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19403654300695)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19403698340119)

4. Edite o perfil desejado, vá em Acesso a Menus e permita o acesso para: **(01.01.01.264 - Histórico Dados cadastrais Futuro: Visualizar | 01.01.01.265 - Histórico Dados cadastrais Futuro: Inserir | 01.01.01.266 - Histórico Dados cadastrais Futuro: Excluir | 01.01.01.267 - Histórico Dados cadastrais Futuro: Editar)** veja:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19403676777879)

5. Para realizar o cadastro ou visualização manual para competência futura, deverá acessar o menu **Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico Dados Cadastrais Futuros:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19403690121367)

![](https://tdn.totvs.com/download/attachments/687158765/image-2023-11-8_17-2-4.png?version=1&modificationDate=1699473725133&api=v2&effects=border-simple,shadow-kn)

6. Visualize ou cadastre conforme demonstração abaixo. Nesta tela podemos alterar (Salario, Seção, Função e ou Rateio Fixo Futuro).

![](https://tdn.totvs.com/download/attachments/687158765/image-2023-11-14_9-46-19.png?version=1&modificationDate=1699965979697&api=v2&effects=border-simple,shadow-kn)

![](https://tdn.totvs.com/download/attachments/687158765/image-2023-11-14_9-50-10.png?version=1&modificationDate=1699966210107&api=v2&effects=border-simple,shadow-kn)

**ATENÇÃO:**

* Não poderá alterar o salário, função, seção ou rateio diretamente no cadastro do funcionário.
* Não poderá inserir alterações futuras diretamente nos anexos de Históricos de Salario, Histórico de Seção ou Histórico de Função.
* Para habilitar a aba Rateio Fixo Futuro deverá acessar o parametrizador Recursos Humanos | Configurações | Requisições | Requisições 2 e marcar o parâmetro "Habilitar o rateio de centro de custos em requisições".

**Saiba Mais:**

[Histórico Dados Cadastrais Futuro](https://tdn.totvs.com/pages/releaseview.action?pageId=687158765#1-3)
