---
content_hash: 5570c6c77244943c808b65f7d1f5f589e4e4e18db73efaddbdcc740223728ad7
fetched_at: '2026-06-29T00:06:24.101043+00:00'
page_id: '224111840'
product: rm
source: tdn-rm
title: Inserindo Logotipo na MDI
type: documentation
url: https://tdn.totvs.com/display/LRM/Inserindo+Logotipo+na+MDI
version: 74
---

Para versões anteriores à 12.1.2209, vide:

# Objetivo

---

Com a reestruturação visual da MDI, ocorrida na versão **12.1.2209**, inserir imagens personalizadas na MDI se tornou ainda mais fácil. Com a remoção dos temas personalizados, que causavam uma perda de desempenho, a exibição de imagens personalizadas não depende mais de um Esquema de Cores específico, podendo ser ativado à qualquer momento.

É necessária permissão de **LEITURA** e **GRAVAÇÃO** no **DIRETÓRIO** onde se encontra a imagem para conseguir incluí-la no RM.

A exibição de imagens na MDI é um recurso pouco performático e por isso, deve ser utilizado com cautela.

# Exibindo uma imagem como logotipo na MDI

---

1. **Habilitando Logotipos** - Primeiramente é necessário permitir que os logotipos sejam exibidos na MDI. Por ser uma configuração que impacta na performance do sistema, para habilitá-lo, é necessário acessar: Ambiente → Parâmetros → Parâmetros Globais → Performance → **Habilitar Logotipos na MDI**. Após ativá-lo, é necessário reiniciar a MDI para aplicar as alterações.
2. **Inserindo Imagens:** Para inserir um novo logotipo ou alterar o existente, acesse Serviços Globais → Administração→ Configurações → Personalizar

Existem três possíveis fluxos em relação à exibição de logotipo, cada uma com suas próprias regras e impactos de performance

* **Exibição de logotipo na MDI desativada:**Esta é a opção mais performática, por não necessitar de carregar nenhuma imagem na MDI.
* **Utilizar imagem da Coligada selecionada:**É possível trocar a imagem toda vez que o contexto é alterado, utilizando a imagem da coligada presente no cadastro de coligadas. Esta é a opção menos performática, pois toda vez que houver uma mudança de contexto, a imagem terá de ser recarregada. Utilize esta opção ciente de que a performance do sistema pode sofrer um declínio
* **Configure o logotipo de sua organização para ser exibido na janela principal do ERP.**: Utilize esta opção para inserir uma imagem personalizada independente do contexto. As restrições desta imagem são possuir no máximo **50KB** e é necessário estar na dimensão **177x86** (Caso esteja com dimensões diferentes, a imagem pode aparecer deformada).

Após as configurações, basta clicar em aplicar e a imagem será atualizada automaticamente. *(Outros clients podem necessitar de ser reiniciados para a aplicação ocorrer com sucesso)*

Atenção!

Esta configuração **não** é possível de uso quando acessado o sistema por meio de **conexão remota** ou **TS**. Para habilitá-la é necessário adicionar a tag "**enableskin**" no atalho do aplicativo RM.exe

Para mais informações sobre a nova MDI .
