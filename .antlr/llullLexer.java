// Generated from /Users/pauvallespi/Desktop/UPC/Q5/LP/Practica2/llull.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class llullLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUM=1, VAR=2, PARL=3, PARR=4, BRACEL=5, BRACER=6, ADD=7, SUB=8, MULT=9, 
		DIV=10, POW=11, GT=12, LT=13, GT_EQ=14, LT_EQ=15, EQUAL=16, NOT_EQ=17, 
		WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUM", "VAR", "PARL", "PARR", "BRACEL", "BRACER", "ADD", "SUB", "MULT", 
			"DIV", "POW", "GT", "LT", "GT_EQ", "LT_EQ", "EQUAL", "NOT_EQ", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
			"'^'", "'>'", "'<'", "'>='", "'<='", "'=='", "'<>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUM", "VAR", "PARL", "PARR", "BRACEL", "BRACER", "ADD", "SUB", 
			"MULT", "DIV", "POW", "GT", "LT", "GT_EQ", "LT_EQ", "EQUAL", "NOT_EQ", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public llullLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "llull.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\\\b\1\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\6\2)\n\2\r\2\16\2*\3\3\3\3\7\3/\n\3\f\3\16\3\62\13\3\3"+
		"\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3"+
		"\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\23\6\23W\n\23\r\23\16\23X\3\23\3\23\2\2\24\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\3\2\6\3\2\62;\4\2C\\c|\6\2\62;C\\aac|\4\2\f\f\"\"\2^\2\3\3\2\2\2"+
		"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2"+
		"\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2"+
		"\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2"+
		"\2\3(\3\2\2\2\5,\3\2\2\2\7\63\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2\r9\3"+
		"\2\2\2\17;\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27C\3\2\2\2\31"+
		"E\3\2\2\2\33G\3\2\2\2\35I\3\2\2\2\37L\3\2\2\2!O\3\2\2\2#R\3\2\2\2%V\3"+
		"\2\2\2\')\t\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\4\3\2\2\2"+
		",\60\t\3\2\2-/\t\4\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2"+
		"\61\6\3\2\2\2\62\60\3\2\2\2\63\64\7*\2\2\64\b\3\2\2\2\65\66\7+\2\2\66"+
		"\n\3\2\2\2\678\7}\2\28\f\3\2\2\29:\7\177\2\2:\16\3\2\2\2;<\7-\2\2<\20"+
		"\3\2\2\2=>\7/\2\2>\22\3\2\2\2?@\7,\2\2@\24\3\2\2\2AB\7\61\2\2B\26\3\2"+
		"\2\2CD\7`\2\2D\30\3\2\2\2EF\7@\2\2F\32\3\2\2\2GH\7>\2\2H\34\3\2\2\2IJ"+
		"\7@\2\2JK\7?\2\2K\36\3\2\2\2LM\7>\2\2MN\7?\2\2N \3\2\2\2OP\7?\2\2PQ\7"+
		"?\2\2Q\"\3\2\2\2RS\7>\2\2ST\7@\2\2T$\3\2\2\2UW\t\5\2\2VU\3\2\2\2WX\3\2"+
		"\2\2XV\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\b\23\2\2[&\3\2\2\2\6\2*\60X\3\b\2"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}