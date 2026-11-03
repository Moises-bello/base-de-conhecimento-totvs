---
content_hash: 7a9f53de21c72b203d6ae92826805286c1daec5b97cdef10b5d20b583810b3a3
fetched_at: '2026-06-29T00:09:35.994636+00:00'
page_id: '425459454'
product: rm
source: tdn-rm
title: Alunos
type: documentation
url: https://tdn.totvs.com/display/LRM/Alunos
version: 87
---

Esta é uma das mais importantes entidades para o Educacional. Aqui uma pessoa se tornará um aluno, sendo identificado sempre pelo seu , conhecido no sistema também pela sigla R.A.  Este registro é a identificação do aluno na instituição, ou seja a identidade estudantil do aluno, assim como temos registros que nos identificam na empresa, ou no meio social, como CPF, Título eleitoral, RG, dentre outros.

Esta identificação será de extrema importância para o sistema bem como para aluno, pois em todos os locais na instituição ele levará este número de R.A. Toda a vida acadêmica do aluno será controlada a partir deste, cursos em que ele será matriculado, eventos no qual participará parte financeira dentro da instituição, dentre outros.

Todas as informações exigidas pelo Ministério da Educação (MEC) para identificação do aluno constam no cadastro, que é dividido em identificação, endereço, documentos, responsáveis e diversos:

Reforma Tributária - (Vigência 01/01/2026)

O endereço completo do aluno torna-se **obrigatório para a geração de movimentos e emissão de NF-e,** para determinação do local da operação e domicílio do tomador para tributação no destino, conforme exigido pela **Reforma Tributária (EC 132/2023).**

# Identificação

Nesta aba são informados dados básicos para que o aluno possa ser reconhecido dentro da instituição: Registro acadêmico, nome, nome social, nome afetivo, naturalidade.

Nomes

* **Nome social**

Conforme Portaria n. 1612/2011 do Ministério da Educação entende-se por nome social aquele pelo qual as pessoas se identificam e são identificadas pela sociedade.

* **Nome afetivo**

Conforme portaria n. 16.785/18 , na aba de identificação foi adicionado o campo Nome afetivo (para crianças e adolescentes que estejam sob guarda familiar adotiva). Ao marcar o parâmetro, **Utiliza tratamento por nome afetivo**, o campo Nome social no cadastro dados básicos do aluno, torna - se o Nome afetivo sem a possibilidade de edição.

Ainda nesta aba temos a informação adicional de aluno canhoto.

Vale ressaltar que o cadastro obedece os critérios parametrizados de unicidade no Gestão de Pessoas (). Além disso, a obrigatoriedade do CPF também pode ser definida, entretanto a parametrização que prevalecerá é a do Totvs Educacional em  e não a do Totvs Gestão de Pessoas em .

Para que os ícones de impressão seja exibidos na tela conforme abaixo, é necessário parametrizar os relatórios 1 e/ou 2 em Configurações | Parâmetros | Secretaria | Relatórios | Grupo: Alunos.

 É possível abrir o cadastro da pessoa a partir do link no campo código.

Mediante parametrização através do Educacional é possível incluir alterar ou excluir [campos complementares](https://tdn.totvs.com/display/LRM/Campos+Complementares+-+TOTVS+Educacional?draft=true) no cadastro de pessoa.

Além disso, é possível visualizar ou realizar alterações na máscara de telefone do cadastro de pessoa,  através do Educacional, na tela [parâmetros do RH](https://tdn.totvs.com/pages/viewpage.action?pageId=825322419).

## Campo Apelido

O campo Apelido que é composto pelo primeiro primeiro nome do conteúdo do campo Nome, porém se o Nome social ou Nome afetivo estiver preenchido, o apelido irá utilizar um dos dois campos para ser preenchido.

A atualização do campo Apelido será feita ao preencher o campo Nome social e ao sair deste campo, quando o conteúdo atual do campo Apelido corresponder ao primeiro nome do campo Nome.  Desta forma o campo Apelido será preenchido com o primeiro nome do campo Nome social. O mesmo vale para o Nome afetivo.

Caso ao salvar o cadastro do aluno o campo Nome social esteja preenchido, ou o campo Nome afetivo esteja preenchido, e o conteúdo do campo Apelido não corresponda respectivamente ao primeiro nome de Nome Social, ou ao primeiro nome de Nome afetivo, o sistema emitirá uma mensagem informativa conforme abaixo:

## Campo E-mail

Ao atualizar a informação do campo e-mail do cadastro do aluno, caso o responsável financeiro cadastrado para o aluno (aba Responsáveis) tenha o mesmo CPF do aluno (aba Documentos), o e-mail do responsável financeiro também será atualizado com a informação de e-mail do aluno.

Caso o campo de e-mail do aluno tenha seu conteúdo removido, ou seja, seja atualizado para nulo, o e-mail do Responsável financeiro permanecerá inalterado, não sendo atualizado para nulo.

Importante

A partir dos patches 12.1.2506.326, 12.1.2510.256 e 12.1.2602.170:

* Cadastros com mais de um endereço de e-mail e separados por ponto e vírgula receberão um aviso em relação ao seu uso na geração de movimento.

# enderecoEndereço

Campos relativos ao endereço do aluno como: CEP, logradouro, número, complemento, bairro, estado, cidade, pais, telefone e outros.

O botão Atualização de Endereço permite ao usuário fazer atualizações nos cadastros de: Mãe, Pai, Responsável Financeiro e Responsável Acadêmico, de acordo com o endereço do aluno e será alterado conforme parametrização das flags (Tel. Residencial, Telefone 3, E-mail, Celular e Fax).

Com a chegada da Reforma Tributária e as novas exigências relacionadas à emissão de notas fiscais, torna-se cada vez mais importante garantir a qualidade das informações cadastrais dos alunos.

Ao salvar o cadastro do aluno, o sistema verifica se o Município e o Estado informados são válidos e existem no cadastro oficial.

* Se o município e o estado não forem encontrados, o sistema permitirá salvar, mas exibirá um aviso.
* Esse aviso é importante porque essa situação pode causar erros na geração de nota fiscal.

**Mensagem exibida:**

"Atenção! O município informado no endereço do aluno não existe no cadastro de municípios (Campo Cidade, aba Endereço/Residencial). Isso poderá causar erro no envio das informações para a nota fiscal."

Ao salvar o cadastro do aluno, o sistema também verifica se o campo Cidade está preenchido.

* Se o campo estiver em branco, o sistema permitirá salvar, mas exibirá um aviso.
* É importante preencher essa informação para evitar problemas na geração de nota fiscal.

**Mensagem exibida:**

"Atenção! O município do endereço do aluno está em branco (Campo Cidade, aba Endereço/Residencial). Preencha essa informação para evitar erros no envio das informações para a nota fiscal."

Disponível a partir das versões : 12.1.2506.248, 12.1.2510.171

Para garantir maior integridade cadastral, evitar inconsistências nos dados e reduzir erros em integrações fiscais e regulatórias, foi criada na parametrização da Secretaria a aba **"Endereço do Aluno"**, contendo os seguintes parâmetros:

* Cidade deve ser obrigatoriamente cadastrada no cadastro de municípios
* Aplicar regra apenas para endereços nacionais

Por padrão, os parâmetros não vêm selecionados. Ao marcar o primeiro parâmetro, o segundo é automaticamente marcado, permanecendo disponível para desmarcação, caso necessário.

Com o parâmetro ativado, o sistema não permite salvar a **descrição da cidade** caso ela não esteja previamente cadastrada no cadastro de municípios.

Quando o parâmetro **"Aplicar regra apenas para endereço nacional"** estivermarcado, a validação será aplicada somente aos endereços nacionais**.**

Para endereços estrangeiros, o sistema continuará seguindo o comportamento atual, permitindo informar a cidade livremente, sem a necessidade de que ela esteja cadastrada na lista oficial de municípios.

Ao desmarcar o parâmetro **"Aplicar regra apenas para endereço nacional"**, a regra também passa a ser aplicada aos endereços estrangeiros, exigindo que a cidade seja selecionada a partir do cadastro oficial de municípios.

Apartir das versões: 12.1.2506.291, 12.1.2510.215, 12.1.2602.133

# Documentos

Nesta aba informamos dados necessários como CPF, RG e Título de Eleitor. Em casos de alunos estrangeiros, é possível informar o passaporte ou registro geral. Vale ressaltar que o CPF poderá ser obrigatório e esta obrigatoriedade pode ser parametrizada em dois lugares diferentes, sendo um no próprio TOTVS Educacional () e outro no Gestão de Pessoas (), entretanto a parametrização do Totvs Educacional que irá prevalecer.

# Responsáveis

Nesta aba informamos o Pai, a Mãe, o responsável financeiro e o responsável acadêmico do aluno.  
   - O responsável financeiro é quem pagará pelos estudos deste aluno.   
      No filtro de seleção de responsável financeiro serão carregados apenas Cliente/Fornecedor com classificação igual a "Cliente" ou "Ambos".  
   - O responsável acadêmico é quem será o responsável pelas reuniões de pais e filhos, entrega de boletins etc.  
Importante ressaltar que o aluno maior de idade que possui CPF pode ser cadastrado como responsável acadêmico e financeiro.

Ao lado de cada campo (pai, mãe, responsável financeiro e responsável acadêmico) existe um botão que irá permitir ao usuário definir quais destes responsáveis será o responsável financeiro do aluno. No caso do campo responsável financeiro será possível incluir o próprio aluno como responsável.

No momento que é clicado no botão que permite cadastrar o pai, a mãe, o aluno ou responsável acadêmico como responsável financeiro o sistema verifica se já existe um cliente/fornecedor com o CPF ou o Homônimo da pessoa informada em um dos campos. Quando identificado um cliente/fornecedor existente será exibido a lista dos encontrados e o usuário poderá selecionar para aproveitar o existente ou criar um novo cliente/fornecedor.

Observação:

Ao cadastrar o PAI/MÃE como responsável financeiro o RM Educacional vai criar um cadastro de cliente com as informações do cadastro de pessoa (Pai/Mãe) no TOTVS Gestão Financeira.

É importante destacar que nas informações de endereço do cadastro de pessoa possui três campos de telefones, sendo, “Telefone 1”, “Telefone 2” e “Telefone 3” estas informações irão popular no cadastro de cliente os campos “Telefone”, “Celular” e “Telefone Comercial” na respectiva ordem.

Esta informação é importante, pois o módulo TOTVS Gestão de Pessoas permite através de parametrização que o título do telefone 1, 2 e 3 do cadastro de pessoa seja customizado, no entanto é importante que ordem dos campos sejam respeitadas.

Caso o responsável financeiro do aluno seja pessoa jurídica, será possível parametrizar [tributos defaults](https://tdn.totvs.com/display/LRM/Tributos+Default+de+Fornecedor) no cadastro do cliente. Desta forma, os tributos PIS, COFINS e CSLL poderão ser carregados automaticamente na [geração de lançamento financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=425459455) das parcelas.

# Diversos

Nesta aba temos informações complementares do aluno como carreira, profissão e outros dados não relevantes ao sistema.

No cadastro do aluno, foi disponibilizado o campo **"Envia dados do destinatário do serviço na geração do movimento"**. Este parâmetro controla a exportação das informações do destinatário para o movimento.

* **Finalidade:** Define se os dados do destinatário (quando o aluno não é o próprio responsável financeiro) devem ser replicados na geração de movimentos.
* **Condição de Uso:** O campo só terá efeito prático se o parâmetro "**Envia dados do destinatário do serviço"** também estiver marcado durante o **processo de geração do movimento**.
* **Importante:** Se o aluno for configurado como seu próprio responsável financeiro, o sistema **nunca envia** os dados do Destinatário do Serviço ao movimento

****Patches disponíveis**:** 12.1.2506.308 · 12.1.2510.234 · 12.1.2602.149

Monitor de documentos para assinatura eletrônica

Para acessar o anexo "Monitor de documentos para assinatura eletrônica", o perfil do usuário deverá ter a seguinte permissão:

* **Educacional | Currículo e Oferta | Aluno e Professor | Alunos | Monitor de documentos enviados para assinatura**

# Pessoas com necessidades educacionais especiais

Nessa sub-aba, da aba de **Identificação**,encontramos os campos relativos as deficiências e necessidades especiais do aluno, com um agrupamento por tipos de deficiência, um grid de detalhes sobre os tipos de deficiência, onde mais de um registro pode ser selecionado e campos textuais relativos a recursos para realização de atividade e acessibilidade:

Os tipos de deficiência no agrupamento são herdados do módulo de recursos humanos, salvo a tipologia "Outros" que é exclusiva do módulo Educacional e pode ter o label customizado na parametrização do Educacional (**15.01 Secretaria → Geral 7/7**). Caso a parametrização esteja em branco a tipologia permanecerá com a label "Outros"

No painel *Detalhes*, é possível adicionar Subdeficiências associadas aos tipos de deficiência que foram selecionados para o aluno. A adição das subdeficiências é filtrada pelos tipos de deficiência, ou seja, estarão disponíveis para cadastro apenas as subdeficiências associadas as deficiências marcadas para o aluno. Vale também ressaltar que as Subdeficiências a serem associadas com o tipo de deficiência personalizado devem obrigatoriamente ser do tipo **Outros**

# Atendimento Especial

Nessa sub-aba da aba de **Identificação** é possível registrar os [atendimentos específicos ou especializados](https://tdn.totvs.com/pages/viewpage.action?pageId=979013297) requeridos pelo aluno, os [recursos necessários para o desempenho de suas atividades,](https://tdn.totvs.com/pages/viewpage.action?pageId=979013353) bem como os [recursos de acessibilidade disponibilizados pela instituição.](https://tdn.totvs.com/pages/viewpage.action?pageId=979013403) Para que seja possível inserir é necessário efetuar o cadastro através do cadastro de Auxiliares  ( Currículo e oferta - Acadêmico - Auxiliares )

Após a realização do cadastro, os itens passam a ser exibidos para seleção e utilização nas respectivas abas do sistema.

Funcionalidade disponível a partir das versões 12.1.2502.195 e 12.1.2506.137.

Informações Complementares

---

[Contratos](http://tdn.totvs.com.br/display/LRM/Contratos+-+EDU)

[Irmãos do Aluno](http://tdn.totvs.com/x/AfxbGQ)

[Anexo - Documentos Solicitados](https://tdn.totvs.com/display/LRM/Documentos+solicitados)

[Enviar documento para assinatura](https://tdn.totvs.com/x/JuVhM) **Novo!!!**

Como Fazer

---

Veja Também

---

[Boletim Técnico Melhorar cópia de responsáveis para responsável financeiro](http://tdn.totvs.com/pages/viewpage.action?pageId=190514954)

[Documentos Solicitados](https://tdn.totvs.com/display/LRM/Tela+-+Documentos+Solicitados)

Recursos Adicionais

---
