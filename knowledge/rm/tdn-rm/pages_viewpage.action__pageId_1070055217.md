---
content_hash: 8298950a7027a8f7d79f23b33fecccf2642411dd926c3f680907d3859c46a857
fetched_at: '2026-06-29T00:05:53.349847+00:00'
page_id: '1070055217'
product: rm
source: tdn-rm
title: PI - Relatórios - Registrar Fontes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070055217
version: 2
---

# Orientação para Utilização de Fontes Personalizadas no Sistema

## Introdução

Este documento explica como instalar e testar fontes personalizadas no sistema para garantir que seus documentos PDF sejam gerados corretamente, mantendo o layout e a aparência desejada.

---

## Por que as fontes precisam ser instaladas?

Quando o sistema converte um documento Word para PDF, ele precisa encontrar exatamente as mesmas fontes utilizadas no seu modelo. Se uma fonte não estiver instalada no servidor, o sistema automaticamente a substitui por outra, o que pode:

* Desalinhar textos e tabelas
* Alterar o número de páginas do documento
* Descaracterizar a identidade visual da sua empresa

---

## Como verificar se uma fonte já está instalada no servidor

### Pelo Windows:

1. Abra o **Painel de Controle**
2. Clique em **"Fontes"** (ou pesquise por "Fontes" no menu Iniciar)
3. Na lista exibida, procure pelo nome da fonte desejada (exemplo: Aptos, Calibri, Arial, etc.)

Se a fonte aparecer na lista, ela já está instalada.

---

## Como instalar uma nova fonte no servidor

### Método padrão (recomendado):

1. **Obtenha o arquivo da fonte** (extensão `.ttf` ou `.otf`)
2. No servidor, **acesse como Administrador**
3. Abra o **Painel de Controle > Fontes**
4. **Arraste o arquivo da fonte** para dentro da pasta de Fontes
5. Aguarde a mensagem de confirmação de instalação

### Método alternativo (clique direito):

1. Localize o arquivo da fonte no servidor
2. Clique com o botão direito sobre o arquivo
3. Selecione **"Instalar"** no menu de contexto

### Outro método:

1. Instalar a fonte desejada via Configurações > Fontes no Windows Server.
2. Copiar as fontes para a pasta global (necessário pois a instalação pode ficar vinculada apenas ao usuário logado):

   Executar no **CMD como Administrador**, um comando de cada vez:

bashEclipsecmd\AppData\Local\Microsoft\Windows\Fonts\\*.ttf") do copy "%f" "C:\Windows\Fonts\" /Y]]>bashEclipsecmd\*.ttf) do reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%~nf (TrueType)" /t REG\_SZ /d "%~nxf" /f]]>

Confira se agora a fonte se encontra instalada globalmente:

Substitua <INSIRAUSUARIOAQU> pelo nome do usuário que fez a instalação da fonte e <INSIRASUAFONTE>\* pelo nome da fonte desejada.

bashcmd

---

## IMPORTANTE: Ambientes Cloud TOTVS

**Se o sistema estiver hospedado na Cloud TOTVS (Protheus Cloud, RM Cloud ou qualquer ambiente gerenciado pela TOTVS), você NÃO tem acesso direto ao servidor para instalar fontes.**

### Procedimento para Cloud TOTVS:

Para instalar ou registrar fontes neste tipo de ambiente, é **obrigatório abrir um chamado (ticket) junto ao suporte da TOTVS Cloud**, solicitando:

1. **A instalação das fontes** no servidor da aplicação
2. **O registro das fontes** no Windows Server (quando necessário)
3. **A reinicialização dos serviços** (IIS ou equivalentes) após a instalação

**No ticket, informe:**

* Nome completo da(s) fonte(s) a serem instaladas
* Arquivos da fonte anexados (formatos .ttf ou .otf)
* Ambiente específico (produção / homologação)
* Data prevista para validação

> ⚠️ **Atenção:** A instalação de fontes em ambientes Cloud TOTVS é restrita e só pode ser realizada pela equipe de infraestrutura da TOTVS. Não tente acessar o servidor diretamente, pois isso viola as políticas de segurança do ambiente.

---

## Como testar se a fonte funciona corretamente

### Teste 1: Verificação básica no Windows

1. No servidor, abra o **Word** (apenas se tiver acesso ao servidor)
2. Crie um documento simples
3. Digite um texto e tente aplicar a fonte instalada
4. Se a fonte aparecer na lista e for aplicada ao texto, a instalação foi bem-sucedida

> **Para ambientes Cloud TOTVS:** O teste diretamente no servidor não será possível. O teste deverá ser realizado via sistema, gerando um PDF após a instalação pela TOTVS.

### Teste 2: Teste completo do sistema

Após instalar a fonte no servidor, **é necessário reiniciar o serviço IIS** (Internet Information Services). Esse passo é essencial para que o sistema de conversão reconheça as novas fontes.

**Passo a passo para reiniciar (a ser feito por quem tem acesso ao servidor):**

1. Acesse o servidor
2. Abra o **IIS Manager**
3. Clique no servidor na árvore lateral esquerda
4. No painel direito, clique em **"Reiniciar"**

Alternativamente (via Prompt de Comando como Administrador):

* Digite o comando: `iisreset`

> **Para ambientes Cloud TOTVS:** A reinicialização deve ser solicitada no mesmo ticket de instalação das fontes, ou em um ticket complementar.

---

## Como criar um documento de teste completo

### Roteiro para validação:

1. **Crie um modelo de teste** no Word com as seguintes características:

   * Utilize a fonte desejada em títulos
   * Utilize a mesma fonte em corpo do texto
   * Utilize a mesma fonte em uma tabela
   * Utilize a mesma fonte em NEGRITO e ITÁLICO
2. **Converta este documento pelo sistema** normalmente
3. **Compare o PDF gerado** com o documento original:

   * ✓ As letras têm o mesmo formato?
   * ✓ Títulos e textos mantêm o tamanho?
   * ✓ As quebras de linha estão iguais?
   * ✓ Tabelas mantiveram suas dimensões?

---

## Problemas comuns e soluções

| Problema | Possível causa | O que fazer |
| --- | --- | --- |
| A fonte não aparece no Word do servidor | Arquivo incompatível ou corrompido | Obter nova cópia da fonte |
| A fonte aparece no Word mas o PDF sai diferente | Serviço IIS não reiniciado | Solicitar reinicialização do IIS |
| O PDF mostra letras genéricas (Arial, Times) | Fonte não está instalada no servidor | Realizar a instalação da fonte |
| Erro de conversão após instalar fonte | Permissão insuficiente | Verificar se instalou como Administrador |
| **Cloud TOTVS: fonte não funciona após solicitação** | Registro incompleto ou serviço não reiniciado | **Abrir novo ticket para a TOTVS com os logs de erro** |

---

## Fontes mais comuns e onde obtê-las

| Fonte | Origem | Observação |
| --- | --- | --- |
| Aptos | Microsoft 365 (padrão desde 2023) | Já vem com Office atualizado |
| Calibri | Microsoft Office | Padrão do Office 2007-2019 |
| Arial | Windows | Nativa do Windows |
| Times New Roman | Windows | Nativa do Windows |
| Fontes personalizadas | Fornecedor / Designer | Necessário licença |

---

## Checklist para homologação

Antes de liberar um novo modelo de documento:

* A fonte foi instalada no servidor (ou solicitada via ticket TOTVS)?
* O servidor foi reiniciado após a instalação (ou solicitado à TOTVS)?
* Foi gerado um PDF de teste com essa fonte?
* O layout do PDF ficou idêntico ao Word original?
* Todas as variações (negrito, itálico, sublinhado) funcionaram?

### Checklist específico para Cloud TOTVS:

* Ticket aberto para a TOTVS com os arquivos das fontes anexados
* Número do protocolo do ticket registrado
* Confirmação da TOTVS de que a instalação foi concluída
* Validação realizada em ambiente de homologação primeiro
* Teste de PDF realizado com sucesso antes de solicitar para produção
